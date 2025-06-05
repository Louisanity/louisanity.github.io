---
title: "Frame Generation in Hilbert Space: Generative Interpolation of Measurement Data for Quantum Parameter Adaptation"
collection: publications
category: conferences
permalink: /publication/2025-04-28-frame-generation-hilbert
excerpt: 'Generative Interpolation reduces quantum measurement overhead in QPA by treating quantum outcomes like video frames and interpolating missing data.'
date: 2025-04-28
venue: 'ICLR 2025 DeLTa Workshop on Deep Generative Models'
paperurl: 'https://openreview.net/forum?id=JNhTrqu39R'
citation: 'Liu, Chen-Yu; Chen, Kuan-Cheng; Chen, Samuel Yen-Chi; Huang, Wei-Jia; &amp; Chang, Yen Jui. (2025). &quot;Frame Generation in Hilbert Space: Generative Interpolation of Measurement Data for Quantum Parameter Adaptation.&quot; <i>ICLR 2025 Workshop on Deep Generative Models</i>.'
---

This paper presents **Generative Interpolation (GI)**, a novel method to reduce measurement overhead in **Quantum Parameter Adaptation (QPA)** for hybrid quantum-classical learning. Key contributions include:

* Treating **quantum measurement probabilities** as analogous to **video frames**, enabling frame-wise estimation of unmeasured basis states.  
* A neural network-based **generative model** fills in missing measurement data, drastically reducing required quantum shots.  
* Enhanced fine-tuning performance for **large language models (LLMs)**, demonstrating practical advantages for QPA under hardware constraints.

The proposed GI framework establishes a connection between **deep generative learning** and **quantum measurement reconstruction**, offering a scalable path forward for variational quantum algorithms.

![Figure: Frame-wise generative interpolation model for quantum measurement completion in QPA tasks.](https://louisanity.github.io/images/frame_generation.jpg)
