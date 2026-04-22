# Chapter 13: Computing Resources for AI Research

:::{admonition} What You Will Learn
:class: tip

- The difference between CPU and GPU computing, and which tasks require which
- How to decide which computing environment is appropriate for your data
- What local, cloud, and University of Michigan resources are available and when to use each
- What a software environment is and why managing it matters across different computing resources
:::


## The Decision Is About Data Before It Is About Power

When researchers think about computing resources, they usually start by asking how much power they need. That is a reasonable question, but it is actually the second question. The first question is what your data allows.

If your dataset contains protected health information, identifiable records, or data covered by a use agreement that restricts where it can be stored, many computing options are off the table regardless of how convenient or powerful they are. Uploading HIPAA-covered data to a personal Google Colab notebook is a compliance violation even if the analysis itself is entirely legitimate.

So the right starting point is a simple decision: is my data sensitive or restricted? The answer determines which resources are available to you, and from that narrowed set you choose based on what your task actually requires computationally.

A rough guide to that decision:

If your data is fully public, synthetic, or contains no human subjects information, you can use essentially any resource, including local, cloud, or university systems, subject to whatever license terms apply.

If your data is identifiable, covered by a data use agreement, or otherwise classified as sensitive, you need to stay within approved institutional systems. Commercial cloud platforms and free notebook services are generally not approved for this data without a specific institutional agreement in place.

If your data is protected health information under HIPAA, you need a HIPAA-compliant environment. Check with your institution's research computing office for approved options.

With that framing established, here is what each category of resource actually offers.


## What Kind of Compute Does Your Task Actually Need?

Before choosing a resource, it helps to have a realistic sense of what your analysis requires. The most important distinction is between CPU-bound and GPU-bound work.

**CPU computing** is what your laptop or desktop does. Modern machines have multiple cores — typically 8 to 16 on a research workstation — which means they can run several tasks in parallel. A wide range of research computing is CPU-bound by nature: statistical modeling, matrix operations on neuroimaging data, cross-validation loops, mixed-effects models, and most tabular data workflows fall into this category. These tasks can sometimes run for hours or days on a laptop. A general linear model (GLM) applied to a large neuroimaging dataset, for instance, computing residuals across many channels and subjects, is a good example of this. The right solution is usually more CPU cores or HPC time, not a GPU.

**GPU computing** becomes relevant when your task involves processing a very large number of simple arithmetic operations simultaneously, which is the computational signature of deep learning. Training a convolutional neural network on medical images, fine-tuning a large language model on text corpora, or running inference across tens of thousands of documents are tasks where a GPU's architecture (thousands of smaller cores designed for parallel arithmetic) provides a qualitative speedup over even a powerful CPU. If you are working with modern deep learning frameworks like PyTorch or TensorFlow and training neural networks of meaningful size, GPU access will make a real difference.

The practical distinction is about the type of parallelism your task requires, not its duration. A week-long GLM computation is CPU-bound and benefits from more cores and memory. A neural network training run that would take a week on CPU might take hours on a GPU, because the math is structured differently.

If your machine has a dedicated NVIDIA GPU, you can check whether it is visible to your environment and actively being used with:

```bash
nvidia-smi
```

This command shows the GPU model, memory usage, and any running processes. If your deep learning code is running but `nvidia-smi` shows no active processes, your framework is likely falling back to CPU. It is worth catching this early before a long training run.


## Local Computing

Your own machine is almost always the right place to start. It is immediately available, requires no access requests, and gives you full control over your environment. For most researchers doing tabular analysis, exploratory work, or prototyping, it will handle everything you need.

The main limitations are memory and, for deep learning, the absence of a dedicated GPU. Most laptops have 16 to 32 GB of RAM, which is adequate for datasets up to several gigabytes. If your dataset is larger than what fits comfortably in memory, or if you are training a neural network and want reasonable training times, you will want to move to a cloud or HPC resource.

One practical note: if your machine does have a dedicated GPU, which is common in gaming computers and some workstations, libraries like PyTorch and TensorFlow can use it automatically, which meaningfully accelerates deep learning workflows without any additional infrastructure.

### Running AI Models Locally

A growing number of researchers are choosing to run large language models directly on their own machines rather than through a cloud API. The motivations are practical. When you use a hosted API, every prompt you send and every response you receive passes through the provider's servers. For most academic use cases that is fine. But if your project involves sensitive interview transcripts, unpublished manuscripts, proprietary datasets, or any data covered by a use agreement, sending that content to an external service may not be appropriate, or may require institutional review that takes time to arrange.

Running a model locally keeps everything on your own hardware. Your prompts, your data, and the model's responses never leave your machine. There is no API key to manage, no usage quota, and no ongoing cost after the initial setup.

The two most widely used tools for this are [LM Studio](https://lmstudio.ai) and [Ollama](https://ollama.com). Both let you download and run open-weight models, such as those from the Llama, Mistral, and Qwen families, without writing any infrastructure code. LM Studio provides a graphical interface that makes it straightforward to browse available models, download them, and start a local chat session. Ollama is command-line based and is often preferred when you want to call a local model from a script or notebook rather than chat with it interactively. Both tools expose a local API endpoint that follows the same interface as the OpenAI API, which means that code written for a cloud model can usually be switched to a local model by changing a single line.

The main constraint is GPU memory (VRAM). A model needs to fit entirely within VRAM to run at a practical speed. The table below gives a rough guide based on 4-bit quantization, which is the default in both LM Studio and Ollama.

| Model size | VRAM needed | Example GPU |
|---|---|---|
| 7B | 4–6 GB | RTX 3060 (12 GB), RTX 4060 |
| 13B | 8–10 GB | RTX 3080 (10 GB), RTX 4070 |
| 30B+ | 20 GB+ | RTX 4090, multi-GPU setup |

For most exploratory research tasks, a 7 to 13 billion parameter model is a reasonable starting point and capable enough to be genuinely useful.

:::{admonition} Apple Silicon and CPU-only inference
:class: note

Apple Silicon Macs are a notable exception to the VRAM rule. Because they use a unified memory architecture where the CPU and GPU share the same memory pool, a MacBook Pro or Mac Mini with 16 or 24 GB of unified memory can run 7 to 13 billion parameter models quite smoothly, without a discrete GPU. This makes Apple Silicon one of the more practical options for researchers who want local inference without a dedicated workstation.

Running a model on CPU only, without any GPU, is technically possible but produces responses slowly enough to be impractical for most research use.
:::

This is not to say local models are always the right choice. For tasks where response quality and speed matter most and the data is not sensitive, a cloud API is simpler and more capable at comparable cost. The decision comes back to the same first question in this chapter: what does your data allow? If the answer is that your data cannot leave your machine, a local model may be exactly what you need.

The companion notebook for Chapter 25 demonstrates how to switch between a cloud API and a local model running through LM Studio with minimal code changes, so you can see what that looks like in practice.


## Cloud Computing

Cloud platforms offer on-demand access to powerful hardware, including GPUs, without requiring you to own or maintain the equipment. The tradeoff is that your data and code leave your local machine, which matters for sensitive data as discussed above.

### Notebook Environments for Pilot Testing: Google Colab and Kaggle Notebooks

Before committing cluster allocations or cloud budgets to a new workflow, it is worth running a small-scale pilot first to confirm that your approach actually works. Google Colab and Kaggle Notebooks are well-suited for exactly this: they let you test code, explore unfamiliar libraries, and run modest experiments without requesting HPC time or incurring cloud charges.

Google Colab provides a hosted Jupyter notebook environment with on-demand access to GPUs on a shared basis. Sessions are temporary: your runtime resets after a period of inactivity and files do not persist by default. But for experimentation, learning, and moderate-scale analysis, it is highly practical. The handbook's AutoGluon tutorial notebook runs in Colab. For persistent storage, you can connect Colab to your Google Drive. GPU availability on the no-cost tier varies and is not guaranteed during peak times; a paid Colab Pro tier offers more reliable access.

Kaggle Notebooks offer a similar environment with a weekly GPU quota, slightly more predictable availability than Colab's no-cost tier, and the advantage of direct access to Kaggle's dataset library. If you are working with a dataset hosted on Kaggle, running your analysis there eliminates the need to download and re-upload data.

Neither platform is appropriate for sensitive, identifiable, or HIPAA-covered data.

### Paid Cloud Platforms

Amazon Web Services, Google Cloud Platform, and Microsoft Azure all offer scalable computing environments where you pay for what you use. These platforms provide far more flexibility than the notebook environments described above. You can configure machines with large amounts of RAM, multiple GPUs, and persistent storage precisely for your workflow.

For most academic researchers, the free notebook options or university HPC resources will be sufficient. Paid cloud compute becomes relevant when a project requires sustained GPU access at a scale that exceeds what university allocations provide, or when a research group has cloud credits through an institutional agreement or grant. AWS SageMaker, Google Vertex AI, and Azure Machine Learning are the respective managed ML platforms on each cloud, but they carry meaningful learning curve and cost for occasional use.


```{admonition} If You're at U-M
:class: note

U-M researchers have access to three HPC systems through Advanced Research Computing (ARC): Great Lakes for general CPU and GPU computing, Armis2 for HIPAA-covered and other compliance-sensitive data, and Lighthouse for large-scale AI and data-intensive workflows. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for details on each cluster, hardware specs, and how to request access.
```


## Setting Up Your Environment

When you move between computing resources, one practical challenge comes up consistently: making sure the software your analysis depends on is actually available and working the way you expect. This is what researchers mean when they talk about a software environment.

A software environment is the collection of packages, libraries, and their specific versions that a piece of code needs in order to run. When you install a package on your laptop, it is only installed there. If you move to a cloud notebook or an HPC cluster, or hand your code to a collaborator, that package may not be present, or a different version may be installed that behaves differently. Managing your environment means making sure the right software is in place wherever your analysis runs.

This matters more than it might seem at first. A package update can quietly change how a function behaves. A collaborator running a slightly older version of a library can get different results from the same code. An HPC cluster may have its own default software versions that conflict with what your project needs. None of these are catastrophic on their own, but they are exactly the kind of thing that wastes hours of debugging time if you are not paying attention to it from the start.

Each computing resource has its own way of handling this. On your local machine, the standard Python approach is to create a virtual environment for each project, keeping its dependencies separate from everything else on the system. Cloud notebook environments like Colab and Kaggle Notebooks come with many popular packages pre-installed, and you can install additional ones within a session. HPC systems typically use a module system, where you load specific software versions before running your jobs. Your institution's research computing office will have documentation on how this works for their particular cluster, and following their official guides is the most reliable approach.

The details of setting up and managing environments, including how to record your dependencies so a collaborator or your future self can reproduce your setup, are covered in [Chapter 22](ch22_reproducibility.md).


## Try This

Before your next analysis, take five minutes to answer three questions: Does my data contain any sensitive, identifiable, or restricted information? How large is my dataset, and will it fit comfortably in my laptop's memory? Does my planned analysis involve training a deep learning model, or is it primarily statistical or matrix-based computation?

Your answers will point you directly to the right resource. If the data is sensitive and HIPAA-covered, the answer is a HIPAA-compliant institutional cluster regardless of anything else. If the data is clean and public and the task is statistical or tabular, your laptop or a university HPC cluster is the right starting point. If you are training a neural network on a large image or text dataset, Colab or a university GPU cluster is where to begin.

That three-question habit takes less time than any setup step, and it avoids the more serious problem of discovering a compliance issue after weeks of analysis.