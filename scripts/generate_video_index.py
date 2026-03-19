#!/usr/bin/env python3
"""
generate_video_index.py

Fetches all playlists and videos from the MIDAS YouTube channel and
generates docs/part4/ch31_video_index.md for the handbook.

Usage
-----
    export YOUTUBE_API_KEY="your_api_key_here"
    python scripts/generate_video_index.py

    # Force a fresh fetch, ignoring the local cache:
    python scripts/generate_video_index.py --no-cache

Getting an API key
------------------
1. Go to https://console.cloud.google.com/
2. Create a project (or select an existing one).
3. Enable "YouTube Data API v3".
4. Under "Credentials", create an API key.
5. The free quota (10,000 units/day) is more than enough for this script.

Dependencies
------------
    pip install google-api-python-client

How it works
------------
The script caches raw API results to scripts/midas_videos_cache.json so
repeated runs do not consume quota. Delete the cache file (or use --no-cache)
to force a fresh fetch. The generated Markdown file is completely overwritten
each run, so it is safe to run whenever the channel is updated.

The topic classification is keyword-based and operates at the playlist level.
If a playlist does not match any keyword group it falls into the "Annual Events
and Symposia" bucket. You can adjust TOPIC_GROUPS below to tune the mapping.

Standalone videos (uploaded to the channel but not added to any curated
playlist) are fetched via the channel's hidden "uploads" playlist and listed
separately at the end of the generated chapter, grouped by year.
"""

import os
import json
import sys
import argparse
import datetime
import re
from pathlib import Path

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Missing dependency. Please run:  pip install google-api-python-client")
    sys.exit(1)


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

CHANNEL_HANDLE = "UM_MIDAS"  # YouTube handle without the @
REPO_ROOT      = Path(__file__).resolve().parent.parent
CACHE_FILE     = Path(__file__).resolve().parent / "midas_videos_cache.json"
OUTPUT_FILE    = REPO_ROOT / "docs" / "part4" / "ch31_video_index.md"

CHANNEL_URL    = "https://www.youtube.com/@UM_MIDAS"
PLAYLISTS_URL  = "https://www.youtube.com/@UM_MIDAS/playlists"


# --------------------------------------------------------------------------- #
# Topic groups
# --------------------------------------------------------------------------- #
# Each group maps a handbook theme to a set of keywords that are matched
# (case-insensitive substring) against playlist titles and descriptions.
# List order determines the order sections appear in the generated chapter.
# --------------------------------------------------------------------------- #

TOPIC_GROUPS = [
    {
        "label": "Understanding How AI Works",
        "description": (
            "These recordings pair well with the early chapters in Part I, "
            "especially the overview of how modern AI systems work and how to "
            "use them effectively through prompting."
        ),
        "chapter_refs": [
            ("How Modern AI Works", "part1/ch02_how_ai_works"),
            ("Prompt Engineering", "part1/ch03_prompt_engineering"),
        ],
        "keywords": [
            "generative ai tutorial",
            "coast-to-coast",
            "under the hood",
            "how generative",
            "diffusion model",
            "large language model",
            "tutorial series",
        ],
    },
    {
        "label": "AI Across the Research Lifecycle",
        "description": (
            "Symposia and keynote recordings that explore AI applications across "
            "many research domains, from experimental design to knowledge sharing. "
            "These are good companions to Part I of the handbook as a whole."
        ),
        "chapter_refs": [
            ("When to Use AI", "part1/ch04_when_to_use_ai"),
            ("Research Planning", "part1/ch06_research_planning"),
        ],
        "keywords": [
            "summit",
            "symposium",
            "science and engineering day",
            "ai in s&e",
            "2025 ai in s",
            "adsa",
            "ai-driven research",
            "ai in science",
            "automated research",
            "colloquium",
            "lecture series",
        ],
    },
    {
        "label": "Ethics, Society, and Responsible AI",
        "description": (
            "A direct complement to the ethics and validation chapters. These "
            "playlists explore fairness, accountability, and the societal consequences "
            "of deploying AI in research and in practice."
        ),
        "chapter_refs": [
            ("Ethics and Privacy", "part1/ch10_ethics_privacy"),
            ("Validation and Interpretation", "part2/ch21_validation_interpretation"),
        ],
        "keywords": [
            "ethical ai",
            "ethics",
            "responsible data",
            "responsible ai",
            "implementing ai in health",
            "lhs colloquium",
            "society lecture",
            "data and ai in society",
        ],
    },
    {
        "label": "Data Analysis and Applied Machine Learning",
        "description": (
            "Hands-on workshop recordings covering data science workflows, "
            "applied modeling, and domain-specific ML use cases. These map closely "
            "to the chapters in Part II."
        ),
        "chapter_refs": [
            ("Exploratory Data Analysis", "part2/ch14_exploratory_analysis"),
            ("AutoML for Tabular Data", "part2/ch17_automl_tabular"),
            ("Pretrained Models for Text and Vision", "part2/ch20_pretrained_text_vision"),
        ],
        "keywords": [
            "computer vision",
            "biodiversity",
            "vesuvius",
            "imaging",
            "scientific instruments",
            "machine learning workshop",
            "data science workshop",
        ],
    },
    {
        "label": "Language Models and Generative AI Applications",
        "description": (
            "Recordings focused on applying large language models to real research "
            "tasks, including retrieval-augmented generation, agentic workflows, and "
            "fine-tuning. These connect closely to the chapters in Part III."
        ),
        "chapter_refs": [
            ("NLP with BERT", "part3/ch23_nlp_with_bert"),
            ("Retrieval-Augmented Generation", "part3/ch24_rag"),
            ("AI Agents", "part3/ch25_ai_agents"),
            ("LLM Evaluation and Fine-Tuning", "part3/ch26_llm_eval_finetuning"),
        ],
        "keywords": [
            "generative ai: from theory",
            "from theory to scientific",
            "language model application",
            "nlp",
            "rag",
            "retrieval",
            "fine-tun",
            "agent",
        ],
    },
]

FALLBACK_GROUP = "Annual Events and Symposia"
FALLBACK_DESC  = (
    "These playlists capture MIDAS annual summits, symposia, panel discussions, "
    "and other community events. They offer a broad view of the research "
    "community's interests each year and are a good way to see how practitioners "
    "from many disciplines are thinking about AI."
)


# --------------------------------------------------------------------------- #
# API helpers
# --------------------------------------------------------------------------- #

def get_api_key() -> str:
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if not key:
        print("ERROR: YOUTUBE_API_KEY environment variable is not set.")
        print("       Set it with:  export YOUTUBE_API_KEY='your_key_here'")
        sys.exit(1)
    return key


def build_service(api_key: str):
    return build("youtube", "v3", developerKey=api_key)


def get_channel_id(service, handle: str) -> str:
    """Resolve a YouTube handle to a channel ID."""
    resp = service.channels().list(
        part="id,snippet",
        forHandle=handle
    ).execute()
    items = resp.get("items", [])
    if not items:
        raise ValueError(f"No channel found for handle @{handle}")
    channel_id = items[0]["id"]
    title      = items[0]["snippet"]["title"]
    print(f"Channel: {title}  (ID: {channel_id})")
    return channel_id


def get_all_playlists(service, channel_id: str) -> list:
    """Fetch every playlist for the channel, handling pagination."""
    playlists, next_page = [], None
    while True:
        kwargs = dict(
            part="snippet,contentDetails",
            channelId=channel_id,
            maxResults=50,
        )
        if next_page:
            kwargs["pageToken"] = next_page
        resp = service.playlists().list(**kwargs).execute()
        for item in resp.get("items", []):
            playlists.append({
                "id":           item["id"],
                "title":        item["snippet"]["title"],
                "description":  item["snippet"].get("description", ""),
                "published_at": item["snippet"]["publishedAt"],
                "video_count":  item["contentDetails"]["itemCount"],
                "url":          f"https://www.youtube.com/playlist?list={item['id']}",
                "thumbnail":    (item["snippet"]
                                 .get("thumbnails", {})
                                 .get("medium", {})
                                 .get("url", "")),
            })
        next_page = resp.get("nextPageToken")
        if not next_page:
            break
    return playlists


def get_playlist_videos(service, playlist_id: str) -> list:
    """Fetch all video entries for one playlist, handling pagination."""
    videos, next_page = [], None
    while True:
        kwargs = dict(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
        )
        if next_page:
            kwargs["pageToken"] = next_page
        resp = service.playlistItems().list(**kwargs).execute()
        for item in resp.get("items", []):
            sn     = item["snippet"]
            vid_id = sn.get("resourceId", {}).get("videoId", "")
            # Skip deleted / private videos
            if sn.get("title") in ("Deleted video", "Private video"):
                continue
            videos.append({
                "title":        sn["title"],
                "description":  sn.get("description", ""),
                "published_at": sn.get("publishedAt", ""),
                "video_id":     vid_id,
                "url":          (f"https://www.youtube.com/watch?v={vid_id}"
                                 if vid_id else ""),
            })
        next_page = resp.get("nextPageToken")
        if not next_page:
            break
    return videos


def get_uploads_playlist_id(channel_id: str) -> str:
    """
    Every YouTube channel has a hidden 'uploads' playlist that contains every
    video ever uploaded, including those not in any curated playlist.
    Its ID is always the channel ID with the 'UC' prefix replaced by 'UU'.
    """
    if channel_id.startswith("UC"):
        return "UU" + channel_id[2:]
    raise ValueError(f"Unexpected channel ID format: {channel_id}")


# --------------------------------------------------------------------------- #
# Fetch + cache
# --------------------------------------------------------------------------- #

def fetch_and_cache(use_cache: bool = True) -> dict:
    """Return channel data, either from cache or the YouTube API."""
    if use_cache and CACHE_FILE.exists():
        print(f"Loading cached data from {CACHE_FILE.name}  "
              f"(use --no-cache to re-fetch)")
        with open(CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)

    print("Fetching fresh data from YouTube Data API v3...")
    api_key = get_api_key()
    service = build_service(api_key)

    channel_id = get_channel_id(service, CHANNEL_HANDLE)

    print("Fetching playlists...")
    playlists = get_all_playlists(service, channel_id)
    print(f"Found {len(playlists)} playlists.")

    for i, pl in enumerate(playlists, 1):
        print(f"  [{i:2d}/{len(playlists)}] {pl['title']}  "
              f"({pl['video_count']} videos)")
        pl["videos"] = get_playlist_videos(service, pl["id"])

    # Collect all video IDs that appear in at least one curated playlist.
    playlist_video_ids: set[str] = set()
    for pl in playlists:
        for v in pl.get("videos", []):
            if v["video_id"]:
                playlist_video_ids.add(v["video_id"])

    # Fetch ALL uploads and find the ones not in any curated playlist.
    uploads_id = get_uploads_playlist_id(channel_id)
    print("Fetching uploads playlist to find standalone videos...")
    all_uploads = get_playlist_videos(service, uploads_id)
    standalone  = [v for v in all_uploads if v["video_id"] not in playlist_video_ids]
    print(f"Found {len(all_uploads)} total uploads, "
          f"{len(standalone)} not in any curated playlist.")

    data = {
        "channel_id":        channel_id,
        "fetched_at":        datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "playlists":         playlists,
        "standalone_videos": standalone,
    }
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved cache to {CACHE_FILE}")
    return data


# --------------------------------------------------------------------------- #
# Classification helpers
# --------------------------------------------------------------------------- #

def classify_playlist(playlist: dict) -> str:
    """Return the topic group label that best matches this playlist."""
    haystack = (playlist["title"] + " " + playlist.get("description", "")).lower()
    for group in TOPIC_GROUPS:
        for kw in group["keywords"]:
            if kw in haystack:
                return group["label"]
    return FALLBACK_GROUP


def extract_year(playlist: dict) -> str:
    """Try to extract a 4-digit year from the playlist title or publish date."""
    m = re.search(r"\b(20[12][0-9])\b", playlist["title"])
    if m:
        return m.group(1)
    pub = playlist.get("published_at", "")
    return pub[:4] if len(pub) >= 4 else ""


# --------------------------------------------------------------------------- #
# Markdown generation
# --------------------------------------------------------------------------- #

def _playlist_row(pl: dict) -> str:
    year  = extract_year(pl)
    count = pl.get("video_count", len(pl.get("videos", [])))
    return f"| [{pl['title']}]({pl['url']}) | {count} | {year} |"


def generate_markdown(data: dict) -> str:
    playlists        = data["playlists"]
    standalone       = data.get("standalone_videos", [])
    fetched_date     = data.get("fetched_at", "")[:10]
    total_in_plists  = sum(pl.get("video_count", len(pl.get("videos", [])))
                           for pl in playlists)
    total_videos     = total_in_plists + len(standalone)

    # Sort playlists newest first
    sorted_pls = sorted(playlists, key=lambda p: extract_year(p), reverse=True)

    # Sort standalone newest first, then group by year
    sorted_standalone = sorted(
        standalone,
        key=lambda v: v.get("published_at", ""),
        reverse=True,
    )
    standalone_by_year: dict[str, list] = {}
    for v in sorted_standalone:
        year = v.get("published_at", "")[:4] or "Unknown"
        standalone_by_year.setdefault(year, []).append(v)

    # Build topic bucket -> [playlists]
    buckets: dict[str, list] = {g["label"]: [] for g in TOPIC_GROUPS}
    buckets[FALLBACK_GROUP] = []
    for pl in sorted_pls:
        buckets[classify_playlist(pl)].append(pl)

    L = []  # lines accumulator

    # ---- Page header ----
    L += [
        "# MIDAS Video Resources",
        "",
        "```{note}",
        f"This index was last generated on {fetched_date}. "
        f"To refresh it with the latest videos, run "
        f"`python scripts/generate_video_index.py` from the repository root "
        f"after setting your `YOUTUBE_API_KEY` environment variable.",
        "```",
        "",
    ]

    # ---- Intro ----
    standalone_note = (
        f" Another {len(standalone)} videos sit outside any playlist."
        if standalone else ""
    )
    L += [
        "MIDAS maintains a growing YouTube library of recorded workshops, "
        "tutorial series, symposia, and invited lectures. As of this writing, "
        f"the channel holds {total_videos} videos across {len(playlists)} playlists.{standalone_note} "
        "This index helps you find recordings that connect to what you are "
        "reading in the handbook, whether you want to see a concept explained "
        "live, hear researchers talk through how they apply a method in their "
        "own work, or work through a full workshop from start to finish.",
        "",
        "The index is organized in three parts. The first groups playlists "
        "by handbook topic, so you can jump directly to recordings that pair "
        "with a chapter you are working through. The second covers standalone "
        "videos not collected into a playlist. The third lists every playlist "
        "in one place, sorted by year, for when you want to browse more freely.",
        "",
    ]

    # ---- By topic ----
    L += ["## Finding Videos by Handbook Topic", ""]

    for group in TOPIC_GROUPS:
        label = group["label"]
        pls   = buckets.get(label, [])
        if not pls:
            continue
        refs_str = ", ".join(
            f"[{name}](../{path})" for name, path in group["chapter_refs"]
        )
        L += [
            f"### {label}",
            "",
            group["description"],
            "",
            f"Related chapters: {refs_str}",
            "",
            "| Playlist | Videos | Year |",
            "|----------|:------:|:----:|",
        ]
        for pl in pls:
            L.append(_playlist_row(pl))
        L.append("")

    # ---- Fallback / events ----
    events = buckets.get(FALLBACK_GROUP, [])
    if events:
        L += [
            f"### {FALLBACK_GROUP}",
            "",
            FALLBACK_DESC,
            "",
            "| Playlist | Videos | Year |",
            "|----------|:------:|:----:|",
        ]
        for pl in events:
            L.append(_playlist_row(pl))
        L.append("")

    # ---- Standalone videos ----
    if sorted_standalone:
        L += [
            "## Other Recordings",
            "",
            "The videos below are on the MIDAS channel but have not been "
            "collected into a playlist. Many of them are recordings of "
            "individual talks, short demos, or event highlights. They are "
            "grouped by year and listed with direct links.",
            "",
        ]
        for year in sorted(standalone_by_year.keys(), reverse=True):
            vids = standalone_by_year[year]
            L += [
                f"### {year}",
                "",
                "| Video | Date |",
                "|-------|------|",
            ]
            for v in vids:
                date  = v.get("published_at", "")[:10]
                title = v["title"].replace("|", "-")
                url   = v.get("url", "")
                link  = f"[{title}]({url})" if url else title
                L.append(f"| {link} | {date} |")
            L.append("")

    # ---- Full playlist table ----
    L += [
        "## All Playlists",
        "",
        "The table below lists every curated playlist on the channel in one "
        "place, sorted from newest to oldest. Use it to browse by year or to "
        "look up a specific workshop series you have heard about.",
        "",
        "| Playlist | Videos | Year |",
        "|----------|:------:|:----:|",
    ]
    for pl in sorted_pls:
        L.append(_playlist_row(pl))
    L += [
        "",
        "---",
        "",
        "You can also browse the full channel directly at "
        f"[youtube.com/@UM_MIDAS]({CHANNEL_URL}/playlists).",
        "",
    ]

    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(
        description="Generate the MIDAS video index for the handbook."
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Ignore cached data and re-fetch everything from the YouTube API.",
    )
    args = parser.parse_args()

    data = fetch_and_cache(use_cache=not args.no_cache)
    md   = generate_markdown(data)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(md, encoding="utf-8")

    total  = sum(pl.get("video_count", len(pl.get("videos", [])))
                 for pl in data["playlists"])
    n_pl   = len(data["playlists"])
    n_sa   = len(data.get("standalone_videos", []))
    print(f"\nWrote {OUTPUT_FILE.relative_to(REPO_ROOT)}")
    print(f"Index covers {total + n_sa} videos: "
          f"{total} in {n_pl} playlists, {n_sa} standalone.")


if __name__ == "__main__":
    main()
