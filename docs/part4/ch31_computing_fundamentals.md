# Chapter 31: Computing Fundamentals

:::{admonition} What You Will Learn
:class: tip

- How to read and understand GPU performance specifications
- What TOPS, TFLOPS, and other compute metrics actually mean
- How memory bandwidth affects real-world model performance
- When different precision levels (FP32, FP16, FP8, FP4) matter for AI workloads
- The difference between on-card memory speed and multi-GPU interconnect bandwidth
- How to estimate inference time from hardware specs
:::

## Why This Matters

When you are working with AI models, you will eventually encounter hardware specifications: a GPU has "312 TFLOPS," a model requires "40 GB of VRAM," an inference pipeline needs "100 billion operations." These numbers are not abstract. They determine how long your analysis takes, how much it costs, and whether a particular approach is even feasible for your data.

The challenge is that the terminology is unfamiliar to many researchers outside computer science. This chapter is a practical guide to understanding compute specifications well enough to make informed decisions about where and how to run your models. You do not need to become a hardware engineer. You do need to read a spec sheet without confusion.

## Throughput and Performance

### TFLOPS and TOPS

The most commonly cited GPU metric is **TFLOPS**, which stands for Tera Floating-Point Operations Per Second. A "floating-point operation" is a single arithmetic calculation involving decimal numbers. "Tera" means one trillion. So 312 TFLOPS means the GPU can perform 312 trillion floating-point operations per second.

The related term **TOPS** stands for Tera Operations Per Second. You will mostly see TOPS on mobile chips and edge devices, such as Apple's Neural Engine or Qualcomm's NPU, where the operations include non-floating-point work like integer arithmetic. When comparing data center GPUs against each other, TFLOPS is the standard unit. Do not mix the two directly when comparing hardware across different contexts.

### Why This Matters: A Concrete Example

Here is why this number matters in practice. Suppose you are fine-tuning a language model on your dataset. The model requires 100 trillion floating-point operations to complete one full pass through your training data. If you are running it on a CPU with 50 GFLOPS (50 billion FLOPS), that computation would take:

100 trillion operations ÷ 50 billion operations per second = 2 million seconds ≈ 23 days

If you move to an NVIDIA H100 GPU with roughly 2,000 TFLOPS at FP16, the same computation takes:

100 trillion operations ÷ 2,000 trillion operations per second ≈ 50 seconds

The difference between 23 days and 50 seconds is not a minor optimization. It is the difference between a feasible project and an impractical one.

### Understanding the Scale

The metric hierarchy is:
- **GFLOPS** = Giga FLOPS = Billions of operations per second
- **TFLOPS** = Tera FLOPS = Trillions of operations per second (1,000 GFLOPS)
- **PFLOPS** = Peta FLOPS = Quadrillions of operations per second (1,000 TFLOPS)

Modern research GPUs range from about 50 TFLOPS (older models like RTX 2080) to 1,000+ TFLOPS (latest consumer-grade and professional GPUs). Supercomputers and specialized AI hardware can reach PFLOPS ranges.

## Memory and Speed

Throughput (TFLOPS) tells you the maximum computation rate, but there is another constraint that often matters more in practice: **memory bandwidth**.

### On-Card Memory Bandwidth

Memory bandwidth is the speed at which data can be read from or written to the GPU's own memory (VRAM), measured in gigabytes per second (GB/s) or terabytes per second (TB/s). If your GPU can perform 1,000 TFLOPS but the memory bandwidth is too low, the GPU spends most of its time waiting for data to arrive rather than doing computation. This is called being "memory-bound" rather than "compute-bound."

Think of it like a factory assembly line. The workers (compute units) can process items very fast (high TFLOPS), but if items arrive too slowly from the warehouse (low memory bandwidth), the workers stand idle waiting for work. The bottleneck is the supply chain, not the workers.

For large language model inference, memory bandwidth is often the limiting factor. A 70 billion parameter model needs to move 140 GB of data from memory to the GPU's compute cores (assuming you are using 2-byte precision). If your GPU has 3,350 GB/s bandwidth, that takes 140 GB ÷ 3,350 GB/s ≈ 0.04 seconds just for the data transfer, before any actual computation happens. In practice, inference latency for large models is often dominated by this data movement rather than by the compute time itself.

### Multi-GPU Interconnect Bandwidth

When a model is too large for a single GPU, it gets split across multiple cards. This is where a second type of bandwidth matters: the speed at which GPUs communicate with each other. NVIDIA's technology for this is called **NVLink**, and it is measured separately from on-card memory bandwidth.

On an A100, NVLink runs at 600 GB/s between cards. H100 and H200 stepped this up to 900 GB/s. The B200 uses NVLink 5.0 at 1,800 GB/s. These numbers are much lower than on-card memory bandwidth (which is in the TB/s range), so multi-GPU communication is a real bottleneck for very large models.

If you are running across multiple machines rather than multiple cards in one server, the connection slows down further. Server-to-server communication typically uses InfiniBand or Ethernet, which operates at tens to a few hundred GB/s. So the three-layer picture looks like this:

- **On-card (VRAM to compute)**: fastest, measured in TB/s
- **Card-to-card within a server (NVLink)**: next, measured in hundreds of GB/s to ~1.8 TB/s on B200
- **Server-to-server (InfiniBand)**: slowest, typically tens to low hundreds of GB/s

For most researchers running inference on a single GPU or a small cluster, on-card bandwidth is the number to watch. If you are working with very large foundation models spread across dozens of GPUs, interconnect bandwidth becomes the binding constraint.

### Latency vs Throughput

These are related but different concepts worth clarifying:

**Throughput** is how much work you can do per unit time (TFLOPS). It answers the question: "How many operations can this GPU do per second?"

**Latency** is the time it takes to complete a single task. It answers the question: "How long does one inference take?" or "How long does one forward pass take?"

You can have high throughput but still experience high latency if you are processing a very computationally expensive task. Conversely, a GPU with lower throughput might have low latency for small, simple tasks because the problem completes quickly even at a slower rate.

For research workflows, latency often matters more than peak throughput. You care more about "how long does my analysis take" than "what is the maximum theoretical compute rate." This is why memory bandwidth and latency become practical concerns even on powerful hardware.

## Model Precision and Trade-offs

An AI model's weights and computations do not all need to use the same numerical precision. There is a deliberate trade-off between precision (how accurately we represent numbers) and efficiency (memory usage and speed).

### The Precision Levels

**FP32 (32-bit floating-point)**
The standard full precision used in most original model training. Each weight and intermediate value is stored as a 32-bit number. This gives high numerical accuracy but uses the most memory and is the slowest to compute.

**FP16 (16-bit floating-point)**
Half the memory and often significantly faster than FP32. Many modern GPUs have specialized hardware for FP16 computation. The main risk is numerical instability in some edge cases, but for most deep learning tasks FP16 works well. Many researchers use FP16 training to reduce memory requirements and speed up compute without much loss in final model quality.

**FP8 (8-bit floating-point)**
Introduced with NVIDIA's H100 in 2022, FP8 is a native hardware format that uses one quarter the memory of FP32 while retaining the floating-point representation that makes it suitable for both training and inference. The H100's Transformer Engine can automatically switch between FP8 and FP16 precision within a single forward pass, which is how it achieves its large performance gains over the A100. Unlike the integer formats described below, FP8 can represent a wide dynamic range of values, which makes it more numerically robust in practice.

**FP4 (4-bit floating-point)**
Native FP4 support arrived with NVIDIA's B200 in 2024. At four bits, four times as many weights fit in the same memory bandwidth compared to FP16, which translates directly into higher throughput for memory-bound inference workloads. Most production inference tasks tolerate FP4 with minimal quality degradation, though tasks requiring precise numerical outputs may see measurable differences. It is worth validating on your specific use case before moving to FP4.

**A note on INT8 and INT4**
You will also encounter INT8 and INT4, which are integer formats rather than floating-point. These belong to a different family called **quantization**, where model weights trained in floating-point are converted (quantized) to lower-precision integers after training. INT8 and INT4 are common in tools like llama.cpp and LM Studio that run models locally on consumer hardware. They are a practical way to fit large models into limited VRAM. The trade-off is that integer quantization can introduce more error than native floating-point formats like FP8, because integers have a fixed range rather than the flexible dynamic range of floating-point numbers. FP8 and FP4 are preferable when the hardware supports them natively.

### When to Use What

- **FP32**: When you are training a model from scratch or fine-tuning and need maximum numerical stability. Also when working with smaller models where memory is not a constraint.
- **FP16 or mixed precision**: When you are training on limited GPU memory or want faster training. Most modern frameworks support automatic mixed precision, which uses FP32 where needed for stability and FP16 elsewhere.
- **FP8**: When you are running inference or training on H100, H200, or newer hardware and want better performance without the quality risk of integer quantization.
- **FP4**: When you are running inference on B200-class hardware and throughput is the priority. Validate quality on your task before deploying.
- **INT8 or INT4**: When running inference on consumer GPUs or local hardware without native FP8/FP4 support. Tools like llama.cpp handle the quantization automatically.

## Practical Reference: Common GPU Specifications

The table below shows approximate specifications for GPUs commonly available to researchers. TFLOPS figures are for FP16 dense (without sparsity), which is the most commonly reported number and the most relevant for typical AI workloads. All figures are for SXM variants of data center GPUs where applicable. These numbers change as new models are released, so always check the manufacturer's official datasheet if you need exact numbers for planning purposes.

| GPU Model | Memory | FP16 TFLOPS | Memory Bandwidth | NVLink Bandwidth | Use Case |
|---|---|---|---|---|---|
| NVIDIA RTX 3080 | 10 GB | ~30 | 760 GB/s | N/A | Gaming, moderate ML training |
| NVIDIA RTX 4090 | 24 GB | ~165 | 1,008 GB/s | N/A | High-end consumer training |
| NVIDIA A100 SXM | 40/80 GB | 312 | 2,039 GB/s | 600 GB/s | Large-scale training, research |
| NVIDIA H100 SXM | 80 GB | 1,979 | 3,350 GB/s | 900 GB/s | Frontier training and inference |
| NVIDIA H200 SXM | 141 GB | 1,979 | 4,800 GB/s | 900 GB/s | Memory-heavy inference, large models |
| NVIDIA L40S | 48 GB | 362 | 864 GB/s | N/A | Inference and serving |
| NVIDIA B200 SXM | 180 GB | 2,250 | 7,700 GB/s | 1,800 GB/s | Largest-scale training and inference |

Sources: NVIDIA official datasheets for A100 (2021), H100 (2022), H200 (2023), and B200 (2024). RTX figures from NVIDIA product pages.

The GPUs in the A100 and above range are primarily available through cloud providers or institutional supercomputers. Consumer GPUs (RTX series) are affordable but have lower memory and throughput, and they do not support NVLink for multi-GPU setups. The H200 and H100 share the same compute architecture; the H200's main advantage is its much larger and faster memory, which makes it better suited for very large model inference. The B200 represents the current frontier and is still scarce and expensive as of this writing.

## Try This

Pick a model you are interested in working with. Look up its parameter count (in billions) and find a spec sheet for a GPU you have access to or are considering. Then answer these questions:

1. How much memory does the model require in FP16? (Rough estimate: parameters × 2 bytes. A 7B parameter model is about 14 GB.)
2. What is the VRAM available on your GPU?
3. Does your model fit? If not, what precision level would you need to use?
4. Estimate the inference time: (model parameters × 2) ÷ (GPU memory bandwidth). The multiplication by 2 converts parameters to bytes at FP16 precision (2 bytes per parameter). Dividing by bandwidth gives a lower bound on how long one inference pass takes, since the GPU must read the entire model from memory at least once per generation step.

This is not a precise calculation, but it gives you a reality check before you try to run something and discover it does not fit or takes hours per example.

## Related Chapters

- [Chapter 13: Computing Resources for AI Research](../part2/ch13_computing_resources.md) — how to choose where to run your models
- [Chapter 2: How AI Systems Actually Work](../part1/ch02_how_ai_works.md) — foundational concepts about neural networks and computation
- [Chapter 20: Working with Pre-trained Models and Embeddings](../part2/ch20_pretrained_text_vision.md) — practical implications of model size and precision when using existing models

---

*Last updated: May 2026*
