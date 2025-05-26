---
title: "Learning quantum phase estimation by variational quantum circuits"
collection: publications
category: conferences
permalink: /publication/2024-06-30-learning-qpe-vqc
excerpt: 'A variational circuit approximation of Quantum Phase Estimation cuts circuit depth and boosts accuracy on noisy quantum devices.'
date: 2024-06-30
venue: '2024 International Joint Conference on Neural Networks (IJCNN)'
paperurl: 'https://ieeexplore.ieee.org/document/10651206'
citation: 'Liu, Chen-Yu; Chen, Kuan-Cheng; &amp; Lin, Chu-Hsuan Abraham. (2024). &quot;Learning quantum phase estimation by variational quantum circuits.&quot; <i>Proceedings of the 2024 International Joint Conference on Neural Networks (IJCNN)</i>, 1–6.'
---

Quantum Phase Estimation (QPE) traditionally depends on an inverse Quantum Fourier Transform, making circuit depth grow rapidly with desired precision. This paper proposes a **variational quantum circuit (VQC) approximation** that:

* **Reduces QPE depth** while preserving estimation accuracy.  
* **Outperforms** noisy QPE simulations and standard QPE on real IBM hardware by mitigating gate errors.  
* Integrates as an intermediate **compiler pass**, promising depth savings for algorithms whose complexity is dominated by QPE.

The results show that adaptive, trainable circuits can improve near-term quantum algorithm performance and remain compatible with future, larger-scale devices.
