# AI-Assisted Reviewing

```{admonition} What You Will Learn
:class: tip

- How AI can help you review and strengthen your own work before submission, for both manuscripts and grants.
- Why using AI when you are the reviewer raises a fundamentally different set of ethical questions than using it on your own work.
- What "whose judgment does this review reflect?" means in practice, and how to use it as your personal decision rule.
- What current journal and funder policies say about AI in peer review.
- A "Try This" exercise at the end to practice AI-assisted self-review on a piece of your own writing.
```

## AI in Review Is Already Happening

A 2025 survey of 1,645 active researchers conducted by Frontiers found that 87% of early-career researchers already use AI tools in their work, and more than half of all reviewers report having tried AI at some point during the peer review process {cite}`Frontiers_2025_AI_peer_review`. Most use it for surface-level tasks: drafting or polishing their written comments, summarizing sections, checking clarity. A smaller group, around 19%, use it to examine methodology or the logic of arguments.

The rules, as most researchers experience them, are unclear. What is allowed? What is ethical? And does it matter whether you are reviewing your own work or someone else's?

The answer to that last question is yes, and it matters a lot. This chapter is organized around that distinction.

---

## Reviewing Your Own Work: A Legitimate Use Case

Before a manuscript or grant goes out for formal review, AI can serve as a useful pre-submission check. Think of it as the equivalent of asking a thoughtful colleague to read a draft, except it is available at 11 at night and will not get tired of your revisions.

Here is what AI does well in this role.

It can read your manuscript as a naive but attentive reader and tell you where the logic breaks down, where an argument feels unsupported, or where a section promises something that a later section does not deliver. This kind of structural feedback is surprisingly hard to get from your own rereading after you have been staring at the same document for weeks. Having something external point at a gap — even if imperfectly — is often enough to make you see it yourself.

For grants specifically, you can ask AI to simulate a skeptical reviewer. Describe your specific aims and ask the tool to identify the most likely criticisms a study section would raise. The AI will not be as sharp as an actual expert in your subfield, and it will miss domain-specific weaknesses that only someone who works in your area would catch. But it will often surface the generic structural problems: aims that are too broad, a significance section that does not clearly connect to the approach, a timeline that does not match the budget. These are the kinds of things that are easy to miss from the inside and relatively easy for AI to flag.

You can also use AI to help with compression and clarity. If you have too many pages, AI can identify what to cut. If a section is dense, AI can suggest ways to make it more readable without losing your meaning. These are language tasks, not scientific tasks, and AI handles them well.

None of this replaces your own judgment or the feedback of real colleagues in your field. But it adds a layer of review that costs you relatively little and often catches real problems before they reach a formal reviewer.

---

## When You Are the Reviewer: A Different Situation Entirely

When you receive a manuscript or a grant proposal for formal peer review, you are in a fundamentally different position. The work you are reviewing is unpublished and confidential. The authors shared it with the journal or funder under an implicit agreement that it would be evaluated by a specific expert — you — and that its contents would not be disclosed beyond the review process.

This confidentiality constraint is the first and most immediate concern with using AI as a reviewer. If you feed manuscript text into any AI system, including an institutionally governed one like UM-GPT, you are potentially exposing unpublished intellectual work in ways the authors never consented to. Even if the data are technically protected within an enterprise environment, the authors did not agree to their work being processed by that system. The confidentiality obligation you accepted when you agreed to review the paper covers AI tools just as it covers human third parties.

NIH makes this explicit: AI is prohibited in peer review under NOT-OD-23-149 {cite}`NIH_NOT_OD_23_149`. NSF takes the same position {cite}`NSF_AI_notice_2023`. Most major journals have adopted similar policies, and the ones that have not yet done so are likely to follow.

```{admonition} If You're at U-M
:class: note

The U-M OVPR specifically discourages AI use in internal peer review for the same confidentiality and bias reasons {cite}`UM_OVPR_AI_guidelines_2025`. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for current UM policy guidance.
```

But confidentiality is only part of the problem. Even a completely private, local AI system running on your own computer — where nothing ever leaves your machine — raises a second and deeper issue.

### The Judgment Problem

When you agreed to review a piece of work, the editor or program officer was asking for your judgment. Not AI's judgment. Not a judgment that AI shaped and you approved. Yours.

Peer review works because it draws on the tacit knowledge of experts: the sense of which questions are genuinely open, which methods are reliable in a specific experimental context, which claims will ring true to the field and which are overclaiming. A language model trained on published literature is reasonably good at recognizing what published science sounds like. It is much less reliable at detecting the subtle methodological flaw that only someone who has run that assay knows to look for, or the incremental contribution that looks significant to a non-expert but adds little to a field where similar work was just published.

If AI does the scientific assessment and you approve it, the review reflects AI's reading of the paper more than yours. That is a misrepresentation of whose expertise the journal or funder was drawing on when they invited you.

### The "Let Me Scan It First" Scenario

A harder case: a senior researcher, genuinely busy, asks AI to generate initial comments on a manuscript, then reviews those comments alongside the paper and makes corrections before submitting. This is tempting because it feels like human judgment is still in the loop. The researcher is reading the paper. They are correcting the AI. They are not just forwarding AI output.

The problem is more subtle than it first appears. When you read a paper after seeing AI-generated comments, your attention is no longer open. You are now responding to the AI's framing of the paper. You will naturally anchor to what it flagged, which makes you more likely to miss what it did not flag. A methodological weakness the model did not recognize may never register because your attention was never directed there. The review that results may feel like yours, but its blind spots were shaped by the model.

There is also a systemic issue worth naming directly. If the peer review system knew that senior faculty were routinely using AI pre-screening to manage review load, it might respond differently: by reducing review burdens, distributing them more equitably, or building AI pre-screening into editorial workflows with transparency. Doing it quietly as a personal workaround keeps the structural problem invisible.

The question to ask yourself is not whether AI touched your review. It is: whose intellectual assessment does this review actually reflect? If you can answer honestly that it reflects yours, and that your reading of the paper was not anchored by AI's framing, you are on solid ground. If you are not sure, that uncertainty is meaningful.

---

## What the Research Says

The Frontiers survey gives a useful picture of where researchers actually are on this {cite}`Frontiers_2025_AI_peer_review`. Early-career researchers use AI in peer review more than any other group, 61% of those with five or fewer years of experience report using it regularly during review, compared to 45% of those with 15 or more years. Many describe it as genuinely helpful for building confidence, managing time, and navigating complex manuscripts when English is not their first language.

At the same time, many share real concerns: they are afraid of using AI incorrectly, they do not know what journals allow, and they are not fully confident in AI's accuracy. These are reasonable worries. The survey also found that 35% of researchers who use AI in their work are essentially self-taught, and 18% report doing nothing specifically to ensure best practice.

This gap between widespread adoption and limited guidance is exactly why the framing matters. The question for this handbook — and for the field — is not whether to prohibit AI in reviewing. That ship has sailed. It is how to use it in ways that preserve the expert judgment the system depends on.

---

## A Practical Framework

Whether you are reviewing your own work or someone else's, the following questions are worth keeping in your head.

For self-review: Is AI helping me see my own work more clearly, or is it generating framing I am accepting without understanding? The test is whether you can defend every part of the submitted work without reference to the AI's comments.

For reviewing others' work: Am I using AI in a way the journal permits, and in a way that preserves the confidentiality I agreed to? And is the scientific judgment in this review genuinely mine?

For the gray areas in between: Ask the editorial office. Journals that have thought carefully about this expect questions, and getting a clear answer in advance is much better than guessing.

---

## Try This

This exercise uses AI to improve your own writing, which is the most straightforwardly appropriate use case.

**Step 1.** Take a section of your own work — a discussion section, a grant specific aims page, or an abstract — and read it through once on your own. Make a mental note of any places that feel uncertain or underdeveloped to you.

**Step 2.** Paste the text into UM-GPT or another institutionally governed AI tool and ask: "Read this as a peer reviewer who is skeptical but fair. What are the two or three most significant concerns you would raise?" Do not give the tool additional context. See what it surfaces.

**Step 3.** Compare the AI's concerns to the ones you identified yourself. Where do they overlap? Where does the AI raise something you missed? Where does it miss something you already knew was a problem?

**Step 4.** Now write a short response — a paragraph — as if you were responding to each concern in a revision letter. This exercise forces you to articulate your scientific reasoning explicitly, which often reveals whether your argument is actually solid or whether it needs more work.

The goal is not to use AI to improve your text directly. It is to use AI as a mirror that helps you see your own reasoning more clearly.

---

## References

```{bibliography}
:filter: docname in docnames
```
