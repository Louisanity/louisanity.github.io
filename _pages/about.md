---
layout: single
permalink: /
title: ""
author_profile: false
classes: wide
redirect_from:
  - /about/
  - /about.html
---

<style>
  /* Homepage profile-card and Bloch-sphere refinement. */
  .lc-home-refined .lc-display-title + .lc-lede {
    margin-top: clamp(1.45rem, 2.4vw, 2.05rem);
  }

  /* Replace the old decorative orbit/circuit arc with a clean Bloch-sphere motif. */
  .lc-home-refined .lc-hero::after {
    content: none !important;
    display: none !important;
  }

  .lc-home-refined .lc-bloch-sphere {
    position: absolute;
    right: clamp(-5.2rem, -6vw, -2.2rem);
    bottom: clamp(-4.6rem, -5vw, -2.2rem);
    width: clamp(260px, 28vw, 430px);
    aspect-ratio: 1 / 1;
    z-index: 0;
    pointer-events: none;
    opacity: 0.78;
  }

  .lc-home-refined .lc-bloch-sphere::before {
    content: "";
    position: absolute;
    inset: 2.5%;
    border-radius: 50%;
    background:
      radial-gradient(circle at 37% 30%, rgba(255,255,255,0.92), rgba(255,255,255,0.20) 28%, transparent 56%),
      radial-gradient(circle at 58% 62%, var(--lc-blue-soft), transparent 58%),
      linear-gradient(135deg, rgba(0,0,205,0.040), rgba(0,0,205,0.010));
    border: 1px solid var(--lc-border-strong);
    box-shadow:
      inset 0 0 0 1px rgba(255,255,255,0.32),
      0 26px 70px rgba(0, 0, 205, 0.10);
  }

  html[data-theme="dark"] .lc-home-refined .lc-bloch-sphere::before {
    background:
      radial-gradient(circle at 37% 30%, rgba(255,255,255,0.14), rgba(255,255,255,0.035) 30%, transparent 58%),
      radial-gradient(circle at 58% 62%, rgba(184,199,255,0.12), transparent 58%),
      linear-gradient(135deg, rgba(184,199,255,0.055), rgba(184,199,255,0.014));
    box-shadow:
      inset 0 0 0 1px rgba(184,199,255,0.12),
      0 26px 70px rgba(0, 0, 0, 0.24);
  }

  .lc-home-refined .lc-bloch-ring {
    position: absolute;
    inset: 11%;
    border: 1px solid var(--lc-border-strong);
    border-radius: 50%;
    opacity: 0.72;
  }

  .lc-home-refined .lc-bloch-ring--equator {
    transform: rotateX(66deg);
  }

  .lc-home-refined .lc-bloch-ring--meridian-a {
    transform: rotate(34deg) rotateX(62deg);
  }

  .lc-home-refined .lc-bloch-ring--meridian-b {
    transform: rotate(-46deg) rotateX(62deg);
    opacity: 0.42;
  }

  .lc-home-refined .lc-bloch-axis {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 1px;
    height: 72%;
    background: linear-gradient(to bottom, transparent, var(--lc-border-strong), transparent);
    transform-origin: center;
    opacity: 0.72;
  }

  .lc-home-refined .lc-bloch-axis--z {
    transform: translate(-50%, -50%);
  }

  .lc-home-refined .lc-bloch-axis--x {
    transform: translate(-50%, -50%) rotate(72deg);
  }

  .lc-home-refined .lc-bloch-axis--y {
    transform: translate(-50%, -50%) rotate(-38deg);
    opacity: 0.44;
  }

  .lc-home-refined .lc-bloch-vector {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 2px;
    height: 39%;
    border-radius: 999px;
    background: linear-gradient(to top, var(--lc-blue), var(--lc-blue-2));
    transform-origin: bottom center;
    transform: translate(-50%, -100%) rotate(42deg);
    box-shadow: 0 12px 28px var(--lc-blue-soft);
  }

  .lc-home-refined .lc-bloch-vector::after {
    content: "";
    position: absolute;
    left: 50%;
    top: -0.18rem;
    width: 0.72rem;
    height: 0.72rem;
    border-radius: 50%;
    transform: translateX(-50%);
    background: var(--lc-blue);
    box-shadow:
      0 0 0 7px var(--lc-blue-soft),
      0 12px 28px rgba(0,0,205,0.22);
  }

  html[data-theme="dark"] .lc-home-refined .lc-bloch-vector::after {
    box-shadow:
      0 0 0 7px rgba(184,199,255,0.16),
      0 12px 28px rgba(184,199,255,0.12);
  }

  .lc-home-refined .lc-bloch-core {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 0.48rem;
    height: 0.48rem;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    background: var(--lc-blue);
    box-shadow: 0 0 0 6px var(--lc-blue-soft);
  }

  /* No state labels: keep the Bloch sphere purely decorative and clean. */
  .lc-home-refined .lc-bloch-label {
    display: none !important;
  }

  /* Hide the old pseudo-element badge to avoid CSS escape rendering issues. */
  .lc-home-refined .lc-identity-card::before {
    content: none !important;
    display: none !important;
  }

  .lc-home-refined .lc-portrait-wrap {
    position: relative;
  }

  .lc-home-refined .lc-photo-badge {
    position: absolute;
    left: 1rem;
    top: 1rem;
    z-index: 2;
    display: inline-flex;
    align-items: center;
    gap: 0.42rem;
    border: 1px solid rgba(255,255,255,0.56);
    border-radius: 999px;
    background: rgba(255,255,255,0.84);
    color: #111827;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    padding: 0.42rem 0.68rem;
    font-size: 0.70rem;
    font-weight: 950;
    letter-spacing: 0.055em;
    line-height: 1;
    text-transform: uppercase;
    white-space: nowrap;
  }

  html[data-theme="dark"] .lc-home-refined .lc-photo-badge {
    background: rgba(25,27,32,0.78);
    color: var(--lc-heading);
    border-color: rgba(184,199,255,0.25);
  }

  .lc-home-refined .lc-identity-role-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.48rem;
    margin: 0.62rem 0 0.88rem;
  }

  .lc-home-refined .lc-identity-title,
  .lc-home-refined .lc-identity-title-secondary {
    display: inline-flex;
    width: fit-content;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--lc-border);
    border-radius: 999px;
    background: var(--lc-blue-soft);
    color: var(--lc-blue);
    padding: 0.34rem 0.58rem;
    font-size: 0.78rem;
    line-height: 1;
    font-weight: 950;
    letter-spacing: 0.045em;
    text-transform: uppercase;
  }

  .lc-home-refined .lc-identity-title-secondary {
    background: var(--lc-surface);
  }

  .lc-home-refined .lc-affiliation-stack {
    display: grid;
    gap: 0.48rem;
    margin: 0.2rem 0 1rem;
  }

  .lc-home-refined .lc-affiliation-item {
    display: flex;
    align-items: center;
    gap: 0.58rem;
    color: var(--lc-muted);
    font-weight: 820;
    line-height: 1.25;
  }

  .lc-home-refined .lc-affiliation-flag {
    display: inline-grid;
    place-items: center;
    width: 1.72rem;
    height: 1.72rem;
    border-radius: 999px;
    border: 1px solid var(--lc-border);
    background: var(--lc-surface);
    box-shadow: 0 8px 22px rgba(15,23,42,0.045);
    font-size: 0.95rem;
    flex: 0 0 auto;
  }

  html[data-theme="dark"] .lc-home-refined .lc-affiliation-flag {
    box-shadow: 0 8px 22px rgba(0,0,0,0.20);
  }

  .lc-home-refined .lc-mini-card span {
    letter-spacing: -0.04em;
  }

  .lc-home-refined .lc-mini-card small {
    font-size: 0.84rem;
    line-height: 1.34;
  }

  @media (max-width: 900px) {
    .lc-home-refined .lc-bloch-sphere {
      right: -7rem;
      bottom: -6rem;
      width: 300px;
      opacity: 0.42;
    }
  }

  @media (max-width: 520px) {
    .lc-home-refined .lc-display-title + .lc-lede {
      margin-top: 1.15rem;
    }

    .lc-home-refined .lc-photo-badge {
      left: 0.75rem;
      top: 0.75rem;
      max-width: calc(100% - 1.5rem);
      font-size: 0.62rem;
      padding: 0.36rem 0.55rem;
    }

    .lc-home-refined .lc-bloch-sphere {
      right: -7.5rem;
      bottom: -5.8rem;
      width: 245px;
      opacity: 0.34;
    }
  }
</style>

<div class="lc-modern-home lc-home-refined">
  <section class="lc-hero" aria-label="Homepage introduction">
    <div class="lc-hero-grid">
      <div class="lc-hero-copy">
        <div class="lc-eyebrow"><span class="lc-status-dot"></span> Quantum AI Scientist</div>
        <h1 class="lc-display-title">Quantum algorithms for <span class="lc-accent">networked</span> quantum systems.</h1>
        <p class="lc-lede">
          My work asks how quantum algorithms can become useful on networked, photonic, and early fault-tolerant platforms. I develop distributed quantum computing architectures, quantum machine learning methods, quantum-HPC benchmarking workflows, and hardware-aware compilation techniques that connect algorithm design with realistic quantum systems.
        </p>
        <div class="lc-cta-row">
          <a class="lc-button" href="{{ '/research/' | relative_url }}">Explore research</a>
          <a class="lc-button-secondary" href="{{ '/publications/' | relative_url }}">View publications</a>
          <a class="lc-button-secondary" href="#contact">Contact</a>
        </div>
      </div>

      <aside class="lc-identity-card" aria-label="Researcher profile">
        <div class="lc-portrait-wrap">
          <div class="lc-photo-badge">Global R&amp;D · Policy-Making</div>
          <picture>
            <source srcset="{{ '/images/louis-profile-gtc.webp' | relative_url }}" type="image/webp">
            <img class="lc-portrait" src="{{ '/images/louis-profile-gtc.jpg' | relative_url }}" alt="Portrait of Dr Kuan-Cheng Louis Chen at NVIDIA GTC">
          </picture>
        </div>

        <h2 class="lc-identity-name">Dr Kuan-Cheng (Louis) Chen</h2>

        <div class="lc-identity-role-pills" aria-label="Professional identity">
          <div class="lc-identity-title">Quantum AI Scientist</div>
          <div class="lc-identity-title-secondary">Guest Lecturer</div>
        </div>

        <div class="lc-affiliation-stack" aria-label="Affiliations">
          <div class="lc-affiliation-item"><span class="lc-affiliation-flag">🇯🇵</span><span>JIJ Europe</span></div>
          <div class="lc-affiliation-item"><span class="lc-affiliation-flag">🇶🇦</span><span>HBKU QC2</span></div>
          <div class="lc-affiliation-item"><span class="lc-affiliation-flag">🇬🇧</span><span>Imperial QuEST</span></div>
          <div class="lc-affiliation-item"><span class="lc-affiliation-flag">🇹🇼</span><span>TSMC</span></div>
        </div>

        <div class="lc-identity-links">
          <a href="mailto:kuan-cheng.chen17@imperial.ac.uk">Email</a>
          <a href="{{ '/cv/' | relative_url }}">CV</a>
          <a href="https://scholar.google.com/citations?user=KoUPm0MAAAAJ&amp;hl=en">Scholar</a>
          <a href="https://github.com/Louisanity">GitHub</a>
        </div>
      </aside>
    </div>

    <div class="lc-mini-grid" aria-label="Research summary">
      <div class="lc-mini-card"><span>Quantum AI</span><small>quantum learning, kernels, and scientific AI workflows</small></div>
      <div class="lc-mini-card"><span>DQC</span><small>networked architectures, compilation, and orchestration</small></div>
      <div class="lc-mini-card"><span>Q-HPC</span><small>benchmarking, simulation, and resource analysis</small></div>
      <div class="lc-mini-card"><span>Photonic QC</span><small>photonic learning and nonlinear quantum resources</small></div>
    </div>

    <div class="lc-bloch-sphere" aria-hidden="true">
      <span class="lc-bloch-ring lc-bloch-ring--equator"></span>
      <span class="lc-bloch-ring lc-bloch-ring--meridian-a"></span>
      <span class="lc-bloch-ring lc-bloch-ring--meridian-b"></span>
      <span class="lc-bloch-axis lc-bloch-axis--z"></span>
      <span class="lc-bloch-axis lc-bloch-axis--x"></span>
      <span class="lc-bloch-axis lc-bloch-axis--y"></span>
      <span class="lc-bloch-vector"></span>
      <span class="lc-bloch-core"></span>
    </div>
  </section>

  <section class="lc-section" aria-labelledby="latest-news">
    <div class="lc-section-head">
      <div>
        <span class="lc-section-kicker">Latest updates</span>
        <h2 id="latest-news">Latest news</h2>
      </div>
    </div>

    <div class="lc-news-grid">
      <article class="lc-news-card">
        <time datetime="2026">2026</time>
        <h3>Extensible universal photonic quantum computing with nonlinearity accepted in Nature Photonics.</h3>
        <p>Collaborative work on scalable photonic quantum computing and nonlinear resources.</p>
      </article>

      <article class="lc-news-card">
        <time datetime="2026">2026</time>
        <h3>Heterogeneous optically detected spin–acoustic resonance accepted in Communications Physics.</h3>
        <p>Molecular thin-film spin–acoustic interfaces for practical quantum sensing technologies.</p>
      </article>

      <article class="lc-news-card">
        <time datetime="2026">2026</time>
        <h3>Adaptive resource orchestration for distributed quantum computing systems accepted in IEEE Internet Computing.</h3>
        <p>System-level orchestration methods for quantum networks and modular quantum processors.</p>
      </article>

      <article class="lc-news-card">
        <time datetime="2025">2025</time>
        <h3>Distributed photonic quantum neural networks recognised at IEEE QCE.</h3>
        <p>Best/distinguished paper activity on distributed quantum learning and photonic quantum computing.</p>
      </article>
    </div>
  </section>

  <section class="lc-section" aria-labelledby="research-themes">
    <span class="lc-section-kicker">Research portfolio</span>
    <h2 id="research-themes">Research themes</h2>
    <p class="lc-section-intro">My research connects algorithmic design, quantum systems engineering, and deployable software workflows for networked and heterogeneous quantum processors.</p>

    <div class="lc-research-grid">
      <article class="lc-research-card">
        <span class="lc-index">01</span>
        <h3>Distributed quantum computing</h3>
        <p>Compilation, resource orchestration, network-aware circuit partitioning, and entanglement-efficient execution across modular processors.</p>
      </article>

      <article class="lc-research-card">
        <span class="lc-index">02</span>
        <h3>Quantum machine learning</h3>
        <p>Quantum kernels, quantum neural networks, parameter-efficient quantum learning, and robust learning workflows for scientific and industrial data.</p>
      </article>

      <article class="lc-research-card">
        <span class="lc-index">03</span>
        <h3>Quantum-HPC and benchmarking</h3>
        <p>Large-scale simulation, quantum software benchmarking, tensor-network workflows, and hardware-aware performance analysis.</p>
      </article>

      <article class="lc-research-card">
        <span class="lc-index">04</span>
        <h3>Photonic quantum computing</h3>
        <p>Photonic processors, distributed photonic learning, optical quantum neural networks, and nonlinear resources for scalable architectures.</p>
      </article>

      <article class="lc-research-card">
        <span class="lc-index">05</span>
        <h3>Quantum algorithms for optimisation</h3>
        <p>Hybrid quantum-classical optimisation, QUBO modelling, finance, energy systems, and combinatorial decision workflows.</p>
      </article>

      <article class="lc-research-card">
        <span class="lc-index">06</span>
        <h3>Practical quantum sensing technologies</h3>
        <p>Spin-based sensing, optically detected resonance, microwave measurement, acoustic interfaces, and room-temperature molecular platforms.</p>
      </article>
    </div>
  </section>

  <section class="lc-section">
    <div class="lc-highlight-strip">
      <div class="lc-highlight-grid">
        <div class="lc-highlight"><strong>Distributed QC</strong><span>network-aware compilation and resource orchestration</span></div>
        <div class="lc-highlight"><strong>Photonic QC</strong><span>learning workflows and nonlinear resources</span></div>
        <div class="lc-highlight"><strong>Quantum-HPC</strong><span>simulation, benchmarking, and resource estimation</span></div>
        <div class="lc-highlight"><strong>QML</strong><span>scientific AI and industrial data applications</span></div>
      </div>
    </div>
  </section>

  <section class="lc-section" aria-labelledby="selected-publications">
    <span class="lc-section-kicker">Selected outputs</span>
    <h2 id="selected-publications">Selected publications</h2>

    <div class="lc-pub-grid">
      <article class="lc-pub-card">
        <span class="lc-venue">IEEE QCE 2025</span>
        <h3>Distributed Quantum Neural Networks on Distributed Photonic Quantum Computing</h3>
        <p>Distributed quantum learning on photonic quantum computing architectures.</p>
      </article>

      <article class="lc-pub-card">
        <span class="lc-venue">IEEE Internet Computing · 2026</span>
        <h3>Adaptive Resource Orchestration for Distributed Quantum Computing Systems</h3>
        <p>Orchestration and system design for distributed quantum computing.</p>
      </article>

      <article class="lc-pub-card">
        <span class="lc-venue">Communications Physics · 2026</span>
        <h3>Heterogeneous Optically Detected Spin–Acoustic Resonance in Molecular Thin Films</h3>
        <p>Spin–acoustic interfaces for practical quantum sensing technologies.</p>
      </article>
    </div>
  </section>

  <section class="lc-section" id="contact" aria-labelledby="contact-title">
    <div class="lc-contact-panel">
      <span class="lc-section-kicker">Contact</span>
      <h2 id="contact-title">Collaboration and research enquiries</h2>
      <p>I am interested in collaborations on distributed quantum computing, quantum-HPC benchmarking, quantum machine learning, photonic quantum computing, and practical quantum sensing technologies.</p>

      <div class="lc-contact-links">
        <a href="mailto:kuan-cheng.chen17@imperial.ac.uk">Email me</a>
        <a href="https://scholar.google.com/citations?user=KoUPm0MAAAAJ&amp;hl=en">Google Scholar</a>
        <a href="https://github.com/Louisanity">GitHub</a>
        <a href="https://www.linkedin.com/in/louis-chen">LinkedIn</a>
      </div>

      <p class="lc-updated">Last updated: June 2026</p>
    </div>
  </section>
</div>
