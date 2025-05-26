---
title: "Quantum-Classical-Quantum Workflow in Quantum-HPC Middleware with GPU Acceleration"
collection: publications
category: conferences
permalink: /publication/2024-07-01-qcq-hpc-gpu
excerpt: 'A distribution-aware QCQ architecture integrates QPUs and GPU-accelerated HPC for efficient quantum simulations and phase transition classification.'
date: 2024-07-01
venue: '2024 International Conference on Quantum Communications, Networking, and Computing (QCNC)'
paperurl: 'https://ieeexplore.ieee.org/document/10628380'
citation: 'Chen, Kuan-Cheng; Li, Xiaoren; Xu, Xiaotian; Wang, Yun-Yuan; &amp; Liu, Chen-Yu. (2024). &quot;Quantum-Classical-Quantum Workflow in Quantum-HPC Middleware with GPU Acceleration.&quot; <i>Proceedings of the 2024 International Conference on Quantum Communications, Networking, and Computing (QCNC)</i>, 304–311.'
---

This paper presents a **Quantum-Classical-Quantum (QCQ)** middleware framework that tightly couples quantum and high-performance classical computing. Key components include:

* **Variational Quantum Eigensolver (VQE)** algorithms executed on QPUs for quantum state preparation.  
* **Tensor Network classifiers** and **Quantum Convolutional Neural Networks (QCNNs)** running on GPU-accelerated classical systems for accurate state identification.  
* Integration of **NVIDIA cuQuantum SDK** and **PennyLane’s Lightning plugin**, achieving up to 10× computational speedup over CPU-based methods.

The QCQ architecture demonstrates 99.5% accuracy in classifying quantum phase transitions in Ising and XXZ models, offering a powerful hybrid paradigm for simulating and understanding complex quantum phenomena at scale.
