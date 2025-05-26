---
title: "Validating Large-Scale Quantum Machine Learning: Efficient Simulation of Quantum Support Vector Machines Using Tensor Networks"
collection: publications
category: manuscripts
permalink: /publication/2025-02-20-qsvm-tensor-networks
excerpt: "We present an efficient tensor-network-based approach for simulating large-scale quantum support vector machines (QSVMs), scaling to hundreds of qubits using cuTensorNet and MPI for multi-GPU acceleration."
date: 2025-02-20
venue: 'Machine Learning: Science and Technology, Volume 6, Number 1'
paperurl: 'https://iopscience.iop.org/article/10.1088/2632-2153/adb4ba'
citation: 'Kuan-Cheng Chen*, Tai-Yue Li, Yun-Yuan Wang, Simon See, Chun-Chieh Wang, Robert Wille, Nan-Yow Chen, An-Cheng Yang, Chun-Yu Lin (2025). &quot;Validating Large-Scale Quantum Machine Learning: Efficient Simulation of Quantum Support Vector Machines Using Tensor Networks.&quot; <i>Machine Learning: Science and Technology</i>, 6(1), 015047. DOI: 10.1088/2632-2153/adb4ba'
doi: '10.1088/2632-2153/adb4ba'
---
We present an efficient tensor-network-based approach for simulating large-scale quantum circuits exemplified by quantum support vector machines (QSVMs). Leveraging the cuTensorNet library on multiple GPUs, our method reduces the exponential runtime growth to near-quadratic scaling with respect to the number of qubits in practical settings.

Traditional state-vector simulations become infeasible beyond ~50 qubits. In contrast, our simulator handles QSVMs with up to 784 qubits, completing simulations within seconds on a single high-performance GPU. Using MPI in multi-GPU settings, we achieve strong linear scalability, further accelerating computation time with increasing dataset sizes.

We validate our framework using MNIST and Fashion-MNIST datasets, achieving robust multiclass classification. This study highlights the potential of QSVMs for high-dimensional data analysis and demonstrates the feasibility of large-qubit simulations within the Quantum-HPC ecosystem.
