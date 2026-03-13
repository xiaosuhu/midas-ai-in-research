# Reproducibility in AI-Assisted Research

:::{admonition} What You Will Learn
:class: tip

- Why reproducibility breaks in computational research, and what actually causes it
- How venv, Conda, and Docker each address a different layer of the problem
- When Conda alone is enough, and when Docker becomes worth the extra effort
- Practical habits for keeping your environment reproducible over time
:::

## It Worked Yesterday

You have probably run into this scenario before. You finish a piece of analysis on your laptop, send the code to a collaborator, and get a message back a few days later saying it does not run. Or you return to a project after six months and find that something has broken, even though you did not change anything. The code is the same. The data is the same. And yet the results are different, or the script just fails.

This is not bad luck. It is a predictable consequence of how Python environments work. Every piece of analysis you write implicitly depends on a specific Python version, specific library versions, and a specific operating system with specific system-level libraries underneath. None of that gets recorded automatically. When any of those assumptions change, the environment your code was written for no longer exists, and the analysis breaks.

Reproducibility in computational research means making those assumptions explicit and preserving them deliberately, so that someone else (or your future self) can run the same analysis and get the same result {cite}`TheturingwayTeam2022`. That sounds straightforward, but in practice it requires thinking about several layers of your software environment, not just the script itself.

## Why Things Break

When people talk about reproducibility problems, the conversation often focuses on data or methodology. But in practice, a huge number of failures come down to environment issues that are much more mundane. The Turing Way community and others working on computational reproducibility have documented this pattern extensively, and the culprits tend to be the same ones over and over {cite}`TheturingwayTeam2022`.

Different operating systems introduce the first layer of fragility. Code that runs on a Mac may not run on Windows or Linux, because the underlying system libraries and file path conventions differ. Even on the same operating system, running different versions of Python can produce different behavior, since the language itself evolves and packages track it. Library versions are another common source of breakage: a function that exists in NumPy 1.23 might have been deprecated or changed in NumPy 2.0. Hidden system dependencies are trickier because you often do not know they are there until they are missing on someone else's machine. And silent updates are perhaps the most insidious, because your environment can drift over time through routine package upgrades without you ever noticing until a result changes or an import fails.

The reason this matters for AI-assisted research specifically is that the workflows are often more complex than a simple script. They may chain together multiple tools, call external APIs, rely on large pretrained models, or involve stochastic components that are sensitive to version-level behavioral differences. The more moving parts, the more places the environment can go wrong.

## A Layered Way to Think About Control

The key insight behind modern environment management is that there is no single tool that solves all of this at once. Different tools operate at different levels of the software stack, and understanding what each one controls (and what it does not) will help you choose the right combination for your situation.

At the most basic level, you have the Python packages themselves: the libraries your code imports. One level down, you have the Python interpreter itself. Beneath that, you have the operating system and its system-level libraries. Each of these can vary independently, and each requires a different kind of tool to pin down.

### Virtual Environments: The Baseline

The simplest tool in Python's ecosystem is the built-in virtual environment, `venv`. When you create a virtual environment, you get an isolated Python installation that is separate from the system Python. Any packages you install inside it do not interfere with other projects, and you can record what you have installed with `pip freeze > requirements.txt`.

For simple projects, this is often enough. If you are working on a single machine, have no complicated compiled dependencies, and just need to isolate package versions between projects, `venv` with a `requirements.txt` file will get the job done. The main limitation is that it does not control the Python version itself (it uses whatever Python you created it with), and it only handles pure Python packages, not compiled dependencies like spatial libraries or anything that links against system binaries.

### Conda: Making Python Environments Repeatable

Conda goes a step further. It manages the Python interpreter itself, not just the packages on top of it. When you create a Conda environment, you can specify exactly which Python version you want. Conda also handles compiled dependencies like BLAS and MKL, which are the underlying linear algebra libraries that NumPy and other numerical packages rely on, and which can be genuinely difficult to install correctly on different operating systems.

The key artifact in a Conda workflow is the `environment.yml` file, which captures your Python version, your Conda packages, and any pip-installed packages {cite}`conda_docs2024`. Someone else can take that file, run `conda env create -f environment.yml`, and reconstruct the same environment on their own machine. This is the reproducibility guarantee that Conda offers.

It is a meaningful guarantee, but it has a boundary. Conda controls the Python environment. It does not control the operating system. If you are working on a Mac and your collaborator is on Linux, Conda environments will not behave identically across those platforms, because the system-level libraries and binary behavior differ underneath. For a lot of research workflows, this is fine. If everyone on your team uses the same OS, or if you are working solo on a short-to-medium-term project, Conda is usually all you need.

### Docker: Controlling the System Your Code Runs On

Docker extends environment control to the level of the operating system itself {cite}`boettiger2015,docker_docs2024`. When you build a Docker image, you specify a base operating system (typically a particular version of Linux), install system libraries, set up a Python environment on top of that, and bundle everything into a single portable artifact. A container is a running instance of that image. Anyone who has Docker installed can pull your image and run your analysis in an environment that is byte-for-byte identical to the one you built it in, regardless of whether they are on Mac, Windows, or Linux.

The Dockerfile is the reproducibility record for that environment. It is a plain text script that specifies, step by step, exactly how the image was built. Like version-controlling your code, version-controlling your Dockerfile means you can always reconstruct the exact environment from any point in the project's history.

What Docker adds over Conda is mainly OS-level isolation and true cross-platform portability. It also makes long-term reproducibility more robust, because a Docker image can be pushed to a registry like Docker Hub and stored there indefinitely. Even if a package is no longer available in the Conda or PyPI channels years from now, the image still works.

The tradeoff is real, though. Docker has a steeper learning curve than Conda. It requires Docker Desktop to be installed, which sometimes involves admin permissions. Iterating on analysis code inside a container is slower than iterating locally, because rebuilding an image takes time. And there is simply more infrastructure to maintain. These are not reasons to avoid Docker, but they are reasons to reach for it when you actually need it rather than using it by default.

## When to Use Which

A reasonable rule of thumb is to start with Conda and add Docker when your situation calls for it.

Conda is usually the right choice when your team is all on the same operating system, when the project has a relatively short or medium time horizon, or when you are working solo and primarily need to isolate package versions between projects. The workflow is familiar to most Python researchers, the tooling is lightweight, and `environment.yml` files are easy to share.

Docker becomes worth the overhead in a few specific situations. If you are collaborating across different operating systems and OS-level differences are causing problems, Docker removes that variable entirely. If you are building something long-term, like a reusable analysis pipeline, a teaching resource, or a deployable application, Docker gives you stronger guarantees that the environment will still work years from now. If you are running analyses in a CI/CD pipeline or on a cluster, Docker containers are often the expected packaging format.

There is also a middle-ground use case that is common in scientific computing: nesting a Conda environment inside a Docker container. This pattern makes sense when you need both OS-level control (from Docker) and fine-grained Python package management (from Conda). The stack looks like this: a host machine with a GPU driver at the bottom, a Docker base image providing a specific Linux environment and CUDA version, a Conda environment inside the container managing Python and its dependencies, and optionally a virtual environment layer on top of that for project-specific packages. This is the setup you will encounter in serious deep learning workflows and GPU-accelerated research pipelines.

## Practical Habits Worth Keeping

Regardless of which tool you use, a few habits make a big difference in practice.

Pin your versions explicitly. Rather than installing `pandas` and getting whatever is current, install `pandas==2.2.1`. Unpinned dependencies are the main reason environments drift. The same logic applies to your Docker base image: use a specific tagged version like `python:3.11.9-slim` rather than `python:latest`, so a rebuild six months from now does not silently change the base.

Commit your environment files to version control. Your `environment.yml` or `requirements.txt` should live in the same repository as your code and be updated whenever you add or change a dependency. This turns your environment specification into a versioned artifact rather than an afterthought.

Document what you installed and why. Environment files record what is installed, but they do not record why certain packages are pinned to specific versions. A short comment in your environment file or README explaining any unusual constraints will save you a lot of confusion later.

If you are using Docker, build your image before you submit a paper or share your code publicly, and make sure you can reconstruct your results from that image. Doing this once before submission is a good forcing function for catching environment issues while you can still fix them.

## Try This

Start with Conda if you are not already using it. Create a new environment for your current project using a specific Python version, install the packages your project needs, and export an `environment.yml` file with `conda env export --from-history > environment.yml`. The `--from-history` flag captures only what you explicitly installed, rather than every transitive dependency, which makes the file much more portable.

Once that works, try sharing the file with a collaborator or creating a fresh environment from it on a different machine (or in a fresh Conda installation). If it reproduces cleanly, you have already solved the most common class of reproducibility failure.

If you are curious about Docker, the companion workshop repository at [github.com/xiaosuhu/midas-env-conda-docker-workshop](https://github.com/xiaosuhu/midas-env-conda-docker-workshop) walks through building a minimal reproducible Python container step by step, including an optional Jupyter interface on the same image.

## Further Reading

For a broader treatment of reproducibility across the full research lifecycle, The Turing Way provides one of the most comprehensive open guides available {cite}`TheturingwayTeam2022`. Boettiger's 2015 paper on Docker for reproducible research is worth reading for the conceptual framing behind containerization in scientific workflows {cite}`boettiger2015`.

## Related Chapters

- [Computing Resources](ch13_computing_resources.md) - Choosing where to run your analysis
- [Validation and Interpretation](ch21_validation_interpretation.md) - Checking that your analysis is correct before sharing it

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)
