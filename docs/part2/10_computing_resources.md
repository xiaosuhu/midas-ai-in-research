# Computing Resources for AI Research

:::{admonition} What You Will Learn
:class: tip

- The difference between CPU and GPU computing, and which tasks require which
- How to decide which computing environment is appropriate for your data
- What local, cloud, and University of Michigan resources are available and when to use each
- How to set up a basic Python environment for data analysis work
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

U-M researchers have access to three HPC systems through Advanced Research Computing (ARC): Great Lakes for general CPU and GPU computing, Armis2 for HIPAA-covered and other compliance-sensitive data, and Lighthouse for large-scale AI and data-intensive workflows. See [AI Resources at the University of Michigan](../part3/20_um_resources.md) for details on each cluster, hardware specs, and how to request access.
```


## Setting Up Your Environment

Regardless of which resource you use, keeping your software environment organized and reproducible matters. The standard approach in Python is to create a virtual environment for each project, which isolates that project's dependencies from everything else on your system.
```python
# Create a virtual environment
python -m venv my_project_env

# Activate it (Mac/Linux)
source my_project_env/bin/activate

# Activate it (Windows)
my_project_env\Scripts\activate

# Install packages
pip install pandas numpy scikit-learn jupyter autogluon
```

Once you have installed your packages, saving a record of them takes one additional command:
```python
pip freeze > requirements.txt
```

That file lets you or a collaborator recreate the same environment later with `pip install -r requirements.txt`. [Chapter 17](17_reproducibility.md) covers reproducibility practices in more depth, including environment management, random seeds, and run logging.

For university HPC systems generally, your institution's research computing office will have documentation on loading modules, creating environments, and submitting batch jobs. Using their official guides rather than reproducing instructions here ensures you always have the most current information.


## Try This

Before your next analysis, take five minutes to answer three questions: Does my data contain any sensitive, identifiable, or restricted information? How large is my dataset, and will it fit comfortably in my laptop's memory? Does my planned analysis involve training a deep learning model, or is it primarily statistical or matrix-based computation?

Your answers will point you directly to the right resource. If the data is sensitive and HIPAA-covered, the answer is a HIPAA-compliant institutional cluster regardless of anything else. If the data is clean and public and the task is statistical or tabular, your laptop or a university HPC cluster is the right starting point. If you are training a neural network on a large image or text dataset, Colab or a university GPU cluster is where to begin.

That three-question habit takes less time than any setup step, and it avoids the more serious problem of discovering a compliance issue after weeks of analysis.