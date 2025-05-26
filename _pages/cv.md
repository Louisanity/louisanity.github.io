---
layout: archive
title:  "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **Ph.D. Quantum Engineering**, Imperial College London &nbsp;•&nbsp; 2020 – 2024  
* **M.Sc. Quantum Engineering**, Imperial College London &nbsp;•&nbsp; 2017 – 2018  
* **M.Sc. Quantum Computing**, Universidad Politécnica de Madrid &nbsp;•&nbsp; 2017  
* **B.Sc. Chemistry (Minor: Financial Engineering)**, National Sun Yat-Sen University &nbsp;•&nbsp; 2012 – 2017  

<br/>

Work experience
======
* **Research Associate**, Imperial College London &nbsp;•&nbsp; 2024 – present  
  * Developing scalable distributed-quantum algorithms, architectures and error-correction protocols  
  * Supervisor: **Prof. Kin K. Leung**  
* **Imperial–TUM Global Fellow**, Technical University of Munich &nbsp;•&nbsp; 2024  
  * Multi-GPU tensor-network simulation of large quantum circuits  
* **Research Intern**, Jij Inc. &nbsp;•&nbsp; 2024  
  * Noise-aware QAOA for combinatorial optimisation  
* **Research Intern**, Classiq Technologies &nbsp;•&nbsp; 2023 – 2024  
  * Automated depth-reduction synthesis flows for quantum circuits  
* **Quantum Policy Assistant**, Regulatory Horizons Council (UK) &nbsp;•&nbsp; 2022 – 2023  
  * Landscape survey and white-paper on UK quantum-technology policy  
* **Qiskit Advocate & Researcher**, IBM Quantum &nbsp;•&nbsp; 2022 – 2024  
  * Hybrid quantum-machine-learning and error-mitigation studies  
* **R&D Device Engineer**, TSMC &nbsp;•&nbsp; 2017 – 2018  
  * Process integration and device modelling for advanced CMOS nodes  

<br/>

Honours & Awards
======
* **John Matthey PhD Prize** (2025)  
* **Imperial Global Fellow** (2023)  
* **TSMC Research Prize** (2022)  
* **National PhD Scholarship – Taiwan** (2021 – 2023)  
* **AWE MSc Prize** (2018)  
* **Deloitte Quantum Climate Challenge – 1st Place** (2024)  

<br/>

Skills
======
* **Programming**: Python, C/C++, Julia, MATLAB, R, LaTeX  
* **Quantum SDKs**: Qiskit, Cirq, PennyLane, Pytket, CUDA-Q  
* **ML / HPC**: PyTorch, TensorFlow, cuTensorNet, multi-GPU programming  
* **EDA / Simulation**: Gem5, TCAD, SPICE  
* **Domains**: Distributed quantum algorithms, error correction, circuit optimisation & resource estimation  

<br/>

Service & Leadership
======
* Chair, **Imperial Quantum Technology Society**  
* Postgraduate Research Academic Officer (Engineering), Imperial College London  
* Reviewer for *Quantum Machine Intelligence*, *Quantum Information Processing*, *Advanced Quantum Technologies*, IEEE CIM  
* Program Committee: **IEEE QCE 2026**, **ICASSP 2025**, **ICMLA 2024–25**  
* Workshop organiser: InfoCom QuNAP 2025, ISCAS Quantum AI 2025  

<br/>

Publications
======
<ul>
{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</ul>

Talks
======
<ul>
{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}
</ul>

Teaching
======
<ul>
{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
</ul>
