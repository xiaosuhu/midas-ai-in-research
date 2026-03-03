# Computing Resources for AI Research

:::{admonition} What You Will Learn
:class: tip

- The difference between CPU and GPU computing, and which tasks require which
- How to decide which computing environment is appropriate for your data
- What local, cloud, and University of Michigan resources are available and when to use each
- How to set up a basic Python environment for data analysis work
:::

---

## The Decision Is About Data Before It Is About Power

When researchers think about computing resources, they usually start by asking how much power they need. That is a reasonable question, but it is actually the second question. The first question is what your data allows.

If your dataset contains protected health information, identifiable records, or data covered by a use agreement that restricts where it can be stored, many computing options are off the table regardless of how convenient or powerful they are. Uploading HIPAA-covered data to a personal Google Colab notebook is a compliance violation even if the analysis itself is entirely legitimate.

So the right starting point is a simple decision: is my data sensitive or restricted? The answer determines which resources are available to you, and from that narrowed set you choose based on what your task actually requires computationally.

A rough guide to that decision:

If your data is fully public, synthetic, or contains no human subjects information, you can use essentially any resource — local, cloud, or university systems — subject to whatever license terms apply.

If your data is identifiable, covered by a data use agreement, or classified as sensitive under U-M policy, you need to stay within approved university systems. Commercial cloud platforms and free notebook services are generally not approved for this data without a specific institutional agreement in place.

If your data is protected health information under HIPAA, you need a HIPAA-compliant environment. At U-M, that means Armis2. Great Lakes is not appropriate for HIPAA data.

With that framing established, here is what each category of resource actually offers.

---

## What Kind of Compute Does Your Task Actually Need?

Before choosing a resource, it helps to have a realistic sense of what your analysis requires. The most important distinction is between CPU-bound and GPU-bound work.

**CPU computing** is what your laptop or desktop does. Modern machines have multiple cores — typically 8 to 16 on a research workstation — which means they can run several tasks in parallel. For most data analysis work involving tabular data, statistical modeling, text processing at moderate scale, and exploratory analysis, a multicore CPU is entirely sufficient. AutoGluon running on CPU can train a competitive ensemble on a moderately sized tabular dataset in a few minutes. You do not need a GPU for this.

**GPU computing** becomes relevant when you are working with tasks that require processing large numbers of operations simultaneously — training deep learning models on images, fine-tuning large language models, or handling very large neural networks. A GPU has thousands of smaller cores designed for exactly this kind of parallel arithmetic. If you are training a convolutional network on medical images, running inference on tens of thousands of documents, or working with any modern large-scale deep learning workflow, GPU access matters considerably.

A practical way to think about it: if your analysis could in principle run overnight on your laptop and produce usable results by morning, you probably do not need GPU access. If you are waiting days for results or running out of memory entirely, it is time to scale up.

---

## Local Computing

Your own machine is almost always the right place to start. It is immediately available, requires no access requests, and gives you full control over your environment. For most researchers doing tabular analysis, exploratory work, or prototyping, it will handle everything you need.

The main limitations are memory and, for deep learning, the absence of a dedicated GPU. Most laptops have 16 to 32 GB of RAM, which is adequate for datasets up to several gigabytes. If your dataset is larger than what fits comfortably in memory, or if you are training a neural network and want reasonable training times, you will want to move to a cloud or HPC resource.

One practical note: if your machine does have a dedicated GPU — common in gaming computers and some workstations — libraries like PyTorch and TensorFlow can use it automatically, which meaningfully accelerates deep learning workflows without any additional infrastructure.

---

## Cloud Computing

Cloud platforms offer on-demand access to powerful hardware, including GPUs, without requiring you to own or maintain the equipment. The tradeoff is that your data and code leave your local machine, which matters for sensitive data as discussed above.

### Free Options: Google Colab and Kaggle Notebooks

For researchers who want GPU access without any cost, two platforms stand out.

Google Colab provides a hosted Jupyter notebook environment with free access to GPUs on a shared basis. Sessions are temporary — your runtime resets after a period of inactivity and files do not persist by default — but for experimentation, learning, and moderate-scale analysis it is highly practical. The handbook's AutoGluon tutorial notebook runs in Colab. For persistent storage, you can connect Colab to your Google Drive. The free tier GPU availability varies and is not guaranteed during peak times; a paid Colab Pro tier offers more reliable access.

Kaggle Notebooks offer a similar environment with free weekly GPU hours, slightly more predictable availability than Colab's free tier, and the advantage of direct access to Kaggle's dataset library. If you are working with a dataset hosted on Kaggle, running your analysis there eliminates the need to download and re-upload data.

Neither platform is appropriate for sensitive, identifiable, or HIPAA-covered data.

### Paid Cloud Platforms

Amazon Web Services, Google Cloud Platform, and Microsoft Azure all offer scalable computing environments where you pay for what you use. These platforms provide far more flexibility than the free notebook services — you can configure machines with large amounts of RAM, multiple GPUs, and persistent storage precisely for your workflow.

For most academic researchers, the free notebook options or university HPC resources will be sufficient. Paid cloud compute becomes relevant when a project requires sustained GPU access at a scale that exceeds what university allocations provide, or when a research group has cloud credits through an institutional agreement or grant. AWS SageMaker, Google Vertex AI, and Azure Machine Learning are the respective managed ML platforms on each cloud, but they carry meaningful learning curve and cost for occasional use.

---

## University of Michigan HPC Resources

For researchers at U-M, the university provides high-performance computing infrastructure through Advanced Research Computing (ARC). The three clusters differ primarily in their data governance requirements and hardware focus.

### Great Lakes

Great Lakes is the university's general-purpose HPC cluster, managed by ARC-TS. It provides access to both CPU and GPU nodes, supports standard research workflows, and is appropriate for most research data that is not protected health information. Researchers receive an allocation of compute hours and can request additional time as needed. Great Lakes runs the standard SLURM job scheduler, and ARC-TS provides documentation and support for getting started. For most U-M researchers whose data does not have special sensitivity requirements, Great Lakes is the right HPC choice.

More information and access: https://arc.umich.edu/greatlakes/

### Armis2

Armis2 is a HIPAA-compliant secure computing environment designed specifically for research involving protected health information. If your project involves electronic health records, clinical data, or any data covered under HIPAA, Armis2 is the appropriate cluster. It operates under stricter data governance controls than Great Lakes, including restrictions on data transfer and network access, and access requires additional approval steps. Researchers working with Michigan Medicine data will typically be directed here.

More information: https://arc.umich.edu/armis2/

### Lighthouse

Lighthouse is a newer ARC-TS resource designed for data-intensive and AI-focused research workflows. It provides access to modern GPU hardware and is oriented toward research groups running large-scale machine learning workloads. If you are scaling beyond what your Great Lakes allocation provides, or you need access to more recent GPU hardware, Lighthouse is worth looking into.

More information: https://arc.umich.edu/lighthouse/

---

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

That file lets you or a collaborator recreate the same environment later with `pip install -r requirements.txt`. It is one of the simplest reproducibility habits you can build into your workflow.

For Great Lakes specifically, ARC-TS maintains documentation on loading modules, creating environments, and submitting jobs through the SLURM scheduler. Rather than reproducing those instructions here, the ARC-TS user guide is the authoritative and up-to-date source: https://arc.umich.edu/greatlakes/user-guide/

---

## Try This

Before your next analysis, take five minutes to answer three questions: Does my data contain any sensitive, identifiable, or restricted information? How large is my dataset, and will it fit comfortably in my laptop's memory? Does my planned analysis involve training a deep learning model, or is it primarily tabular or statistical work?

Your answers will point you directly to the right resource. If the data is sensitive and HIPAA-covered, the answer is Armis2 regardless of anything else. If the data is clean and public and the task is tabular, your laptop is probably fine to start. If you are training a neural network on a large image dataset, Colab or Great Lakes GPU nodes are your natural starting point.

That three-question habit takes less time than any setup step, and it avoids the more serious problem of discovering a compliance issue after weeks of analysis.