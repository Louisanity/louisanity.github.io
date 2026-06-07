---
layout: archive
title: "CV"
permalink: /cv/
author_profile: false
classes: wide lc-interior-shell
redirect_from:
  - /resume
---

{% include base_path %}

<style>
  .page__title,
  .archive__subtitle {
    display: none !important;
  }

  .lc-cv-page-refined {
    width: min(1080px, calc(100vw - 2rem));
    margin-inline: auto;
    color: var(--lc-text);
  }

  .lc-cv-page-refined .lc-page-hero {
    grid-template-columns: minmax(0, 1fr) minmax(260px, 0.34fr);
  }

  .lc-cv-profile-panel {
    display: grid;
    gap: 0.62rem;
    align-content: center;
  }

  .lc-cv-profile-panel > div {
    border: 1px solid var(--lc-border);
    border-radius: 18px;
    background: rgba(255,255,255,0.56);
    padding: 0.78rem 0.82rem;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }

  html[data-theme="dark"] .lc-cv-profile-panel > div {
    background: rgba(255,255,255,0.035);
  }

  .lc-cv-profile-panel strong {
    display: block;
    color: var(--lc-blue);
    font-size: clamp(1.05rem, 1.6vw, 1.3rem);
    line-height: 1.05;
    letter-spacing: -0.035em;
    font-weight: 950;
    margin-bottom: 0.28rem;
  }

  .lc-cv-profile-panel span {
    display: block;
    color: var(--lc-muted);
    font-size: 0.78rem;
    line-height: 1.35;
    font-weight: 760;
  }

  .lc-cv-section {
    margin: clamp(1.45rem, 3vw, 2rem) 0;
  }

  .lc-cv-section-head {
    margin-bottom: 0.86rem;
  }

  .lc-cv-section h2 {
    margin: 0;
    color: var(--lc-heading);
    font-size: clamp(1.45rem, 2.45vw, 2rem);
    line-height: 1.08;
    letter-spacing: -0.045em;
    font-weight: 950;
  }

  .lc-cv-role-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.82rem;
  }

  .lc-cv-role-card {
    position: relative;
    overflow: hidden;
    border: 1px solid var(--lc-border);
    border-radius: 22px;
    background:
      radial-gradient(circle at 12% 0%, var(--lc-blue-soft), transparent 30%),
      linear-gradient(180deg, rgba(255,255,255,0.70), rgba(255,255,255,0.96));
    box-shadow: var(--lc-shadow-card);
    padding: 1rem 1rem 1.05rem;
  }

  html[data-theme="dark"] .lc-cv-role-card {
    background:
      radial-gradient(circle at 12% 0%, rgba(184,199,255,0.12), transparent 30%),
      linear-gradient(180deg, rgba(31,33,37,0.78), rgba(31,33,37,0.96));
  }

  .lc-cv-role-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 4px;
    height: 100%;
    background: var(--lc-blue);
    opacity: 0.9;
  }

  .lc-cv-role-card h3 {
    margin: 0;
    color: var(--lc-heading);
    font-size: 1.05rem;
    line-height: 1.2;
    letter-spacing: -0.03em;
    font-weight: 950;
  }

  .lc-cv-role-card .lc-cv-role-title {
    display: inline-flex;
    width: fit-content;
    margin: 0.62rem 0 0.58rem;
    border: 1px solid var(--lc-border);
    border-radius: 999px;
    background: var(--lc-blue-soft);
    color: var(--lc-blue);
    padding: 0.3rem 0.52rem;
    font-size: 0.72rem;
    line-height: 1;
    font-weight: 920;
    letter-spacing: 0.035em;
    text-transform: uppercase;
  }

  .lc-cv-role-card p {
    margin: 0;
    color: var(--lc-muted);
    font-size: 0.9rem;
    line-height: 1.56;
    font-weight: 620;
  }

  .lc-cv-education-list {
    display: grid;
    gap: 0.72rem;
  }

  .lc-cv-education-item {
    display: grid;
    grid-template-columns: 7.6rem minmax(0, 1fr);
    gap: 0.85rem;
    align-items: start;
    border: 1px solid var(--lc-border);
    border-radius: 22px;
    background:
      linear-gradient(180deg, rgba(255,255,255,0.62), rgba(255,255,255,0.94));
    box-shadow: 0 12px 34px rgba(15,23,42,0.055);
    padding: 0.92rem 1rem;
  }

  html[data-theme="dark"] .lc-cv-education-item {
    background:
      linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.025));
    box-shadow: 0 12px 34px rgba(0,0,0,0.18);
  }

  .lc-cv-date-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: fit-content;
    border-radius: 999px;
    background: var(--lc-blue-soft);
    color: var(--lc-blue);
    padding: 0.36rem 0.62rem;
    font-size: 0.78rem;
    line-height: 1;
    font-weight: 950;
    letter-spacing: -0.01em;
    white-space: nowrap;
  }

  .lc-cv-education-body h3 {
    margin: 0;
    color: var(--lc-heading);
    font-size: clamp(1rem, 1.35vw, 1.16rem);
    line-height: 1.24;
    letter-spacing: -0.03em;
    font-weight: 950;
  }

  .lc-cv-education-body p {
    margin: 0.34rem 0 0;
    color: var(--lc-muted);
    font-size: 0.94rem;
    line-height: 1.45;
    font-weight: 640;
  }

  .lc-cv-feature-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.82rem;
  }

  .lc-cv-card,
  .lc-cv-wide-card {
    position: relative;
    overflow: hidden;
    border: 1px solid var(--lc-border);
    border-radius: 22px;
    background: rgba(255,255,255,0.66);
    box-shadow: var(--lc-shadow-card);
    padding: 0.95rem 1rem;
  }

  html[data-theme="dark"] .lc-cv-card,
  html[data-theme="dark"] .lc-cv-wide-card {
    background: rgba(255,255,255,0.035);
  }

  .lc-cv-card h3,
  .lc-cv-wide-card h3 {
    margin: 0 0 0.42rem;
    color: var(--lc-heading);
    font-size: 1rem;
    line-height: 1.22;
    letter-spacing: -0.025em;
    font-weight: 930;
  }

  .lc-cv-card p,
  .lc-cv-wide-card p {
    margin: 0;
    color: var(--lc-muted);
    font-size: 0.9rem;
    line-height: 1.56;
    font-weight: 620;
  }

  .lc-cv-tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.48rem;
  }

  .lc-cv-tag-cloud span {
    display: inline-flex;
    align-items: center;
    border: 1px solid var(--lc-border);
    border-radius: 999px;
    background: rgba(255,255,255,0.62);
    color: var(--lc-blue);
    padding: 0.38rem 0.58rem;
    font-size: 0.78rem;
    line-height: 1;
    font-weight: 850;
  }

  html[data-theme="dark"] .lc-cv-tag-cloud span {
    background: rgba(255,255,255,0.035);
  }

  @media (max-width: 980px) {
    .lc-cv-page-refined .lc-page-hero {
      grid-template-columns: 1fr;
    }

    .lc-cv-profile-panel {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .lc-cv-role-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 720px) {
    .lc-cv-page-refined {
      width: min(100%, calc(100vw - 1rem));
    }

    .lc-cv-profile-panel,
    .lc-cv-feature-grid {
      grid-template-columns: 1fr;
    }

    .lc-cv-education-item {
      grid-template-columns: 1fr;
      gap: 0.55rem;
      padding: 0.86rem 0.88rem;
    }
  }
</style>

<div class="lc-modern-page lc-interior-page lc-cv-page-refined">
  <section class="lc-page-hero lc-page-hero-compact" aria-label="CV introduction">
    <div class="lc-page-hero-copy">
      <div class="lc-eyebrow"><span class="lc-status-dot"></span> Academic CV</div>
      <h1>Curriculum vitae</h1>
      <p>
        Research profile of Dr Kuan-Cheng (Louis) Chen across quantum algorithms, distributed quantum computing,
        quantum machine learning, photonic quantum computing, quantum-HPC benchmarking, and practical quantum sensing technologies.
      </p>
      <div class="lc-cta-row lc-cta-row-compact">
        <a class="lc-button" href="{{ '/publications/' | relative_url }}">Publications</a>
        <a class="lc-button-secondary" href="{{ '/research/' | relative_url }}">Research</a>
        <a class="lc-button-secondary" href="mailto:kuan-cheng.chen17@imperial.ac.uk">Email</a>
      </div>
    </div>

    <div class="lc-cv-profile-panel" aria-label="CV highlights">
      <div>
        <strong>Quantum AI Scientist</strong>
        <span>Quantum algorithms, learning, software, and systems</span>
      </div>
      <div>
        <strong>Global R&amp;D</strong>
        <span>Industrial quantum workflows and benchmarking</span>
      </div>
      <div>
        <strong>Policy-making</strong>
        <span>Quantum technology regulation and translation</span>
      </div>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-current-roles">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Current roles</span>
      <h2 id="cv-current-roles">Appointments</h2>
    </div>

    <div class="lc-cv-role-grid">
      <article class="lc-cv-role-card">
        <h3>Imperial College London</h3>
        <span class="lc-cv-role-title">Guest Lecturer · Imperial QuEST</span>
        <p>Distributed quantum computing, quantum algorithms, quantum software, compilation, and benchmarking.</p>
      </article>

      <article class="lc-cv-role-card">
        <h3>JIJ Europe Ltd.</h3>
        <span class="lc-cv-role-title">Global R&amp;D Manager</span>
        <p>Industrial quantum algorithms, benchmarking, quantum-HPC workflows, quantum optimisation, and quantum machine learning applications.</p>
      </article>

      <article class="lc-cv-role-card">
        <h3>HBKU QC2</h3>
        <span class="lc-cv-role-title">Research Professor</span>
        <p>Quantum large language models, quantum data-centric machine learning, and quantum AI workflows for scientific and engineering applications.</p>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-education">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Academic training</span>
      <h2 id="cv-education">Education</h2>
    </div>

    <div class="lc-cv-education-list">
      <article class="lc-cv-education-item">
        <span class="lc-cv-date-pill">2020–2024</span>
        <div class="lc-cv-education-body">
          <h3>Ph.D. Quantum Engineering</h3>
          <p>Imperial College London</p>
        </div>
      </article>

      <article class="lc-cv-education-item">
        <span class="lc-cv-date-pill">2024</span>
        <div class="lc-cv-education-body">
          <h3>Visiting Researcher</h3>
          <p>Technical University of Munich</p>
        </div>
      </article>

      <article class="lc-cv-education-item">
        <span class="lc-cv-date-pill">2017–2018</span>
        <div class="lc-cv-education-body">
          <h3>M.Sc. Quantum Engineering</h3>
          <p>Imperial College London</p>
        </div>
      </article>

      <article class="lc-cv-education-item">
        <span class="lc-cv-date-pill">2014–2015</span>
        <div class="lc-cv-education-body">
          <h3>Exchange Study in Quantum Chemistry</h3>
          <p>Tsinghua University</p>
        </div>
      </article>

      <article class="lc-cv-education-item">
        <span class="lc-cv-date-pill">2012–2017</span>
        <div class="lc-cv-education-body">
          <h3>B.Sc. Chemistry; Double Major in Business / Financial Engineering</h3>
          <p>National Sun Yat-sen University</p>
        </div>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-research-interests">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Research scope</span>
      <h2 id="cv-research-interests">Research interests</h2>
    </div>

    <div class="lc-cv-tag-cloud">
      <span>Distributed quantum computing</span>
      <span>Quantum networks</span>
      <span>Quantum machine learning</span>
      <span>Photonic quantum computing</span>
      <span>Quantum-HPC benchmarking</span>
      <span>Tensor-network simulation</span>
      <span>Quantum circuit compilation</span>
      <span>Resource estimation</span>
      <span>Early fault-tolerant quantum computing</span>
      <span>Quantum optimisation</span>
      <span>Quantum finance</span>
      <span>Power systems</span>
      <span>Practical quantum sensing technologies</span>
      <span>Spin–acoustic interfaces</span>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-awards">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Recognition</span>
      <h2 id="cv-awards">Honours and awards</h2>
    </div>

    <div class="lc-cv-feature-grid">
      <article class="lc-cv-card">
        <h3>QTC Distinguished Paper Award / Best Paper</h3>
        <p>IEEE QCE 2025.</p>
      </article>
      <article class="lc-cv-card">
        <h3>John Matthey Prize</h3>
        <p>2025 doctoral research recognition.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Imperial Global Fellow</h3>
        <p>Selected for international collaboration and research impact.</p>
      </article>
      <article class="lc-cv-card">
        <h3>TSMC Research Prize</h3>
        <p>Recognition for research excellence.</p>
      </article>
      <article class="lc-cv-card">
        <h3>National PhD Scholarship — Taiwan</h3>
        <p>Competitive national merit-based funding for doctoral study.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Hackathon awards</h3>
        <p>IBM Quantum Hackathon 1st; Deloitte Quantum Climate Challenge 1st; Xanadu QHack 2nd; Blaise Pascal Quantum Challenge 3rd; MIT iQuHack 3rd.</p>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-funding">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Funding</span>
      <h2 id="cv-funding">Selected grants and funding</h2>
    </div>

    <div class="lc-cv-feature-grid">
      <article class="lc-cv-card">
        <h3>Imperial QuEST Seed Funding</h3>
        <p>Realizing Quantum Optical Neural Networks through Programmable Photonic Processors, 2024.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Imperial QuEST Seed Funding</h3>
        <p>Distributed Photonic Quantum Neural Networks for Distributed Learning in Medical Neuroimaging, 2025.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Imperial–TUM Global Fellows Fund</h3>
        <p>Quantum Software for Distributed Quantum Computing.</p>
      </article>
      <article class="lc-cv-card">
        <h3>ICoNYCh Exchange Fund</h3>
        <p>Quantum Machine Learning in Quantum–HPC.</p>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-service">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Service</span>
      <h2 id="cv-service">Professional activities</h2>
    </div>

    <div class="lc-cv-feature-grid">
      <article class="lc-cv-wide-card">
        <h3>Editorial and reviewing</h3>
        <p>Editor for APL Machine Learning Quantum Artificial Intelligence Special Topic. Reviewer for quantum, AI, computational intelligence, and conference venues including IEEE QCE, ICASSP, IJCNN, ICMLA, and ICALP.</p>
      </article>
      <article class="lc-cv-wide-card">
        <h3>Workshop organisation</h3>
        <p>INFOCOM QuNAP Workshop 2025; ISCAS Special Session 2025; IEEE QAI Special Session 2025; QCNC QC4C3 2026; IEEE QCE QuBench 2026.</p>
      </article>
      <article class="lc-cv-wide-card">
        <h3>Policy and mentorship</h3>
        <p>Contributor to quantum technology regulation activities. Mentor through IBM Quantum, QOSF, QWorld QIntern, and Imperial Quantum Technology Society.</p>
      </article>
      <article class="lc-cv-wide-card">
        <h3>Invited talks</h3>
        <p>DCTL Manchester 2025; ICS Salt Lake City 2025; Quantum Innovation Summit Dubai 2024; MRS Cancun 2023.</p>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-skills">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Technical profile</span>
      <h2 id="cv-skills">Skills</h2>
    </div>

    <div class="lc-cv-feature-grid">
      <article class="lc-cv-card">
        <h3>Programming</h3>
        <p>Python, C/C++, Julia, MATLAB, Java, R, LaTeX, Linux.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Quantum SDKs</h3>
        <p>Qiskit, Cirq, PennyLane, Pytket, CUDA-Q.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Machine learning and HPC</h3>
        <p>PyTorch, TensorFlow, tensor networks, CUDA, cuTensorNet, MPI.</p>
      </article>
      <article class="lc-cv-card">
        <h3>Simulation and devices</h3>
        <p>Gem5, TCAD, SPICE, microwave and electron-paramagnetic-resonance instrumentation.</p>
      </article>
    </div>
  </section>

  <section class="lc-cv-section" aria-labelledby="cv-output">
    <div class="lc-cv-section-head">
      <span class="lc-section-kicker">Selected work</span>
      <h2 id="cv-output">Research outputs</h2>
    </div>

    <article class="lc-cv-wide-card">
      <h3>Publication archive and open research profile</h3>
      <p>The complete publication archive and selected work are available through the publications page and Google Scholar profile.</p>
      <div class="lc-cta-row lc-cta-row-compact">
        <a class="lc-button" href="{{ '/publications/' | relative_url }}">View publications</a>
        <a class="lc-button-secondary" href="https://scholar.google.com/citations?user=KoUPm0MAAAAJ&amp;hl=en">Google Scholar</a>
        <a class="lc-button-secondary" href="https://github.com/Louisanity">GitHub</a>
      </div>
    </article>
  </section>
</div>
