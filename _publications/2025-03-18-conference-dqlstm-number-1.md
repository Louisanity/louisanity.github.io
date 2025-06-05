---
title: "Toward Large-Scale Distributed Quantum Long Short-Term Memory with Modular Quantum Computers"
collection: publications
category: conferences
permalink: /publication/2025-05-12-distributed-qlstm-iwcmc
excerpt: 'This work introduces a scalable Distributed QLSTM framework using modular quantum computers for large-scale temporal sequence modeling.'
date: 2025-05-12
venue: 'IWCMC 2025 – The 21st International Wireless Communications & Mobile Computing Conference'
paperurl: 'https://arxiv.org/pdf/2503.14088'
citation: 'Chen, Kuan-Cheng; Chen, Samuel Yen-Chi; Liu, Chen-Yu; &amp; Leung, Kin K. (2025). &quot;Toward Large-Scale Distributed Quantum Long Short-Term Memory with Modular Quantum Computers.&quot; <i>Proceedings of IWCMC 2025 – The 21st International Wireless Communications & Mobile Computing Conference</i>.'
---

This paper presents a **Distributed Quantum Long Short-Term Memory (QLSTM)** framework designed for execution on **modular quantum computing architectures**, enabling scalability on **Noisy Intermediate-Scale Quantum (NISQ)** devices. Highlights include:

* Embedding **variational quantum circuits (VQCs)** into LSTM cells to capture **long-range temporal dependencies**.  
* Partitioning VQCs into subcircuits for execution across a network of **Quantum Processing Units (QPUs)**.  
* Validation on challenging sequence tasks, such as **damped harmonic oscillators** and **NARMA sequences**, demonstrating **stable convergence** and enhanced training efficiency.

This approach lays the groundwork for integrating **distributed quantum learning** into future **hybrid quantum-classical HPC systems**, supporting large-scale AI applications in dynamic environments.

![Figure: Modular QPU architecture and benchmark results for Distributed QLSTM applied to temporal sequence modeling.](https://louisanity.github.io/images/distqlstm.jpg)
