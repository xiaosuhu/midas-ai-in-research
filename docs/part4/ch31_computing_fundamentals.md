# Chapter 31: Computing Fundamentals

:::{admonition} What You Will Learn
:class: tip

- How to read and understand GPU performance specifications
- What TOPS, TFLOPS, and other compute metrics actually mean
- How memory bandwidth affects real-world model performance
- When different precision levels (FP32, FP16, INT8) matter
- How to estimate inference time from hardware specs
:::

## Why This Matters

When you are working with AI models, you will eventually encounter hardware specifications: a GPU has "312 TFLOPS," a model requires "40 GB of VRAM," an inference pipeline needs "100 billion operations." These numbers are not abstract. They determine how long your analysis takes, how much it costs, and whether a particular approach is even feasible for your data.

The challenge is that the terminology is unfamiliar to many researchers outside computer science. This chapter is a practical guide to understanding compute specifications well enough to make informed decisions about where and how to run your models. You do not need to become a hardware engineer. You do need to read a spec sheet without confusion.

## Throughput and Performance

### TFLOPS and TOPS

The most commonly cited GPU metric is **TFLOPS**, which stands for Tera Floating-Point Operations Per Second. A "floating-point operation" is a single arithmetic calculation involving decimal numbers. "Tera" means one trillion. So 312 TFLOPS means the GPU can perform 312 trillion floating-point operations per second.

The related term **TOPS** stands for Tera Operations Per Second and is more general — it applies to operations that are not necessarily floating-point (integer operations, for instance). In practice, the terms are used somewhat interchangeably, though TFLOPS is more common when discussing deep learning hardware.

### Why This Matters: A Concrete Example

Here is why this number matters in practice. Suppose you are fine-tuning a language model on your dataset. The model requires 100 trillion floating-point operations to complete one full pass through your training data. If you are running it on a CPU with 50 GFLOPS (50 billion FLOPS), that computation would take:

100 trillion operations ÷ 50 billion operations per second = 2 million seconds ≈ 23 days

If you move to an NVIDIA H100 GPU with 1.4 PETA FLOPS (1.4 × 10^15 FLOPS, or 1,400 TFLOPS), the same computation takes:

100 trillion operations ÷ 1,400 trillion operations per second ≈ 71 seconds

The difference between 23 days and 71 seconds is not a minor optimization. It is the difference between a feasible project and an impractical one.

### Understanding the Scale

The metric hierarchy is:
- **GFLOPS** = Giga FLOPS = Billions of operations per second
- **TFLOPS** = Tera FLOPS = Trillions of operations per second (1,000 GFLOPS)
- **PFLOPS** = Peta FLOPS = Quadrillions of operations per second (1,000 TFLOPS)

Modern research GPUs range from about 50 TFLOPS (older models like RTX 2080) to 1,000+ TFLOPS (latest consumer-grade and professional GPUs). Supercomputers and specialized AI hardware can reach PFLOPS ranges.

## Memory and Speed

Throughput (TFLOPS) tells you the maximum computation rate, but there is another constraint that often matters more in practice: **memory bandwidth**.

### Memory Bandwidth

Memory bandwidth is the speed at which data can be read from or written to the GPU's memory, measured in gigabytes per second (GB/s). If your GPU can perform 1,000 TFLOPS but the memory bandwidth is too low, the GPU spends most of its time waiting for data to arrive rather than doing computation. This is called being "memory-bound" rather than "compute-bound."

Think of it like a factory assembly line. The workers (compute units) can process items very fast (high TFLOPS), but if items arrive too slowly from the warehouse (low memory bandwidth), the workers stand idle waiting for work. The bottleneck is the supply chain, not the workers.

For large language model inference, memory bandwidth is often the limiting factor. A 70 billion parameter model needs to move 140 GB of data from memory to the GPU's compute cores (assuming you are using 2-byte precision). If your GPU has 900 GB/s bandwidth, that takes 140 GB ÷ 900 GB/s ≈ 0.15 seconds just for the data transfer, before any actual computation happens. In practice, inference latency for large models is often dominated by this data movement rather than by the compute time itself.

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

**INT8 (8-bit integer)**
Quantization to 8-bit integers uses 1/4 the memory of FP32. This is commonly used for inference (not training) because inference does not require gradients and is more forgiving of quantization. Many production systems quantize models to INT8 to reduce memory footprint and increase throughput.

**INT4 (4-bit integer) and Other Low-Precision Formats**
Extreme quantization used when memory is the primary constraint. A 7 billion parameter model in INT4 takes about 3.5 GB of VRAM (versus 28 GB in FP32). This is how large models can run on consumer GPUs. The trade-off is reduced numerical precision, but for many inference tasks the difference in output quality is minimal.

### When to Use What

- **FP32**: When you are training a model from scratch or fine-tuning and need maximum numerical stability. Also when working with smaller models where memory is not a constraint.
- **FP16 or mixed precision**: When you are training on limited GPU memory or want faster training. Most modern frameworks support automatic mixed precision, which uses FP32 where needed for stability and FP16 elsewhere.
- **INT8**: When you are doing inference on quantized models in production or when you want to maximize throughput.
- **INT4**: When running inference on very large models on consumer hardware. Trade-off is acceptable for inference because you are not backpropagating.

## Practical Reference: Common GPU Specifications

The table below shows approximate specifications for GPUs commonly available to researchers. These numbers change as new models are released, so always check the official specification if you need exact numbers.

| GPU Model | Memory | TFLOPS (FP32) | Memory Bandwidth | Use Case |
|---|---|---|---|---|
| NVIDIA RTX 3080 | 10 GB | ~30 | 760 GB/s | Gaming, moderate ML training |
| NVIDIA RTX 4090 | 24 GB | ~83 | 1,036 GB/s | High-end consumer training |
| NVIDIA A100 | 40/80 GB | 312 | 2,039 GB/s | Large-scale training, research |
| NVIDIA H100 | 80 GB | 1,456 | 3,350 GB/s | Frontier training and inference |
| NVIDIA L40S | 48 GB | 362 | 960 GB/s | Inference and serving |

The GPUs in the A100 and H100 range are primarily available through cloud providers or institutional supercomputers. Consumer GPUs (RTX series) are affordable but have lower memory and throughput. The right choice depends on your model size, data, and available budget.

## Try This

Pick a model you are interested in working with. Look up its parameter count (in billions) and find a spec sheet for a GPU you have access to or are considering. Then answer these questions:

1. How much memory does the model require in FP32? (Rough estimate: parameters × 4 bytes. A 7B parameter model is about 28 GB.)
2. What is the VRAM available on your GPU?
3. Does your model fit? If not, what precision level would you need to use?
4. Estimate the inference time: (model parameters × 2) ÷ (GPU memory bandwidth). This is a lower bound on how long one inference pass takes.

This is not a precise calculation, but it gives you a reality check before you try to run something and discover it does not fit or takes hours per example.

## Related Chapters

- [Chapter 13: Computing Resources for AI Research](../part2/ch13_computing_resources.md) — how to choose where to run your models
- [Chapter 2: How AI Systems Actually Work](../part1/ch02_how_ai_works.md) — foundational concepts about neural networks and computation
- [Chapter 20: Working with Pre-trained Models and Embeddings](../part2/ch20_pretrained_text_vision.md) — practical implications of model size and precision when using existing models
