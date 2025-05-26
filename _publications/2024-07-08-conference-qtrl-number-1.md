---
title: "QTRL: Toward Practical Quantum Reinforcement Learning via Quantum-Train"
collection: publications
category: conferences
permalink: /publication/2024-07-08-qtrl-quantum-train
excerpt: 'QTRL trains classical policy models using quantum circuits, avoiding quantum inference and enabling practical quantum reinforcement learning.'
date: 2024-07-08
venue: '2024 IEEE International Conference on Quantum Computing and Engineering (QCE)'
paperurl: 'https://arxiv.org/pdf/2407.03241'
citation: 'Liu, Chen-Yu; Lin, Chu-Hsuan Abraham; Yang, Chao-Han Huck; Chen, Kuan-Cheng; &amp; Hsieh, Min-Hsiu. (2024). &quot;QTRL: Toward Practical Quantum Reinforcement Learning via Quantum-Train.&quot; <i>Proceedings of the 2024 IEEE International Conference on Quantum Computing and Engineering (QCE)</i>.'
---

**QTRL** introduces a novel quantum-classical hybrid approach for reinforcement learning using the **Quantum-Train** method. It overcomes key limitations in quantum reinforcement learning, including:

* **No quantum inference**: final trained model is classical, ensuring fast, low-latency inference using standard hardware.  
* **Efficient training**: leverages a quantum circuit to reduce classical policy network parameters by a **polylogarithmic factor**.  
* **Practical deployment**: eliminates data encoding overhead and reduces quantum hardware dependency.

By shifting the quantum computation to the training phase only, QTRL offers a scalable and cost-effective strategy for applying quantum machine learning to real-world decision-making systems.
