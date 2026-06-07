---
layout: single
title: "Intellectual Property Notice"
permalink: /NOTICE/
author_profile: false
classes: wide lc-interior-shell
---

<style>
  .page__title,
  .archive__subtitle {
    display: none !important;
  }

  .lc-notice-page {
    width: min(920px, calc(100vw - 2rem));
    margin: clamp(1.4rem, 3vw, 2.4rem) auto;
    color: var(--lc-text, #333942);
  }

  .lc-legal-document {
    position: relative;
    overflow: hidden;
    border: 1px solid var(--lc-border, rgba(0, 0, 205, 0.14));
    border-radius: 28px;
    background:
      radial-gradient(circle at 10% 8%, var(--lc-blue-soft, rgba(0, 0, 205, 0.08)), transparent 30%),
      linear-gradient(180deg, rgba(255,255,255,0.82), rgba(255,255,255,0.98));
    box-shadow: var(--lc-shadow-soft, 0 24px 80px rgba(15, 23, 42, 0.10));
    padding: clamp(1.15rem, 3vw, 2rem);
  }

  html[data-theme="dark"] .lc-legal-document {
    background:
      radial-gradient(circle at 10% 8%, rgba(184,199,255,0.12), transparent 30%),
      linear-gradient(180deg, rgba(31,33,37,0.84), rgba(31,33,37,0.98));
  }

  .lc-legal-document::before {
    content: "";
    position: absolute;
    inset: 0;
    pointer-events: none;
    background-image:
      linear-gradient(var(--lc-border, rgba(0,0,205,0.14)) 1px, transparent 1px),
      linear-gradient(90deg, var(--lc-border, rgba(0,0,205,0.14)) 1px, transparent 1px);
    background-size: 56px 56px;
    -webkit-mask-image: radial-gradient(circle at 82% 10%, black, transparent 68%);
    mask-image: radial-gradient(circle at 82% 10%, black, transparent 68%);
    opacity: 0.18;
  }

  .lc-legal-document > * {
    position: relative;
    z-index: 1;
  }

  .lc-legal-header {
    display: grid;
    gap: 0.85rem;
    border-bottom: 1px solid var(--lc-border, rgba(0,0,205,0.14));
    padding-bottom: 1.25rem;
    margin-bottom: 1.25rem;
  }

  .lc-legal-kicker {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    border: 1px solid var(--lc-border, rgba(0,0,205,0.14));
    border-radius: 999px;
    background: var(--lc-blue-soft, rgba(0,0,205,0.08));
    color: var(--lc-blue, #0000CD);
    padding: 0.38rem 0.66rem;
    font-size: 0.72rem;
    line-height: 1;
    font-weight: 950;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }

  .lc-legal-title {
    margin: 0;
    color: var(--lc-heading, #242a32);
    font-size: clamp(2rem, 4.4vw, 3.4rem);
    line-height: 0.98;
    letter-spacing: -0.065em;
    font-weight: 950;
  }

  .lc-legal-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
  }

  .lc-legal-meta span {
    display: inline-flex;
    align-items: center;
    border: 1px solid var(--lc-border, rgba(0,0,205,0.14));
    border-radius: 999px;
    background: rgba(255,255,255,0.62);
    color: var(--lc-muted, #667085);
    padding: 0.38rem 0.62rem;
    font-size: 0.76rem;
    line-height: 1;
    font-weight: 820;
  }

  html[data-theme="dark"] .lc-legal-meta span {
    background: rgba(255,255,255,0.035);
  }

  .lc-legal-alert {
    border: 1px solid var(--lc-border-strong, rgba(0,0,205,0.24));
    border-radius: 20px;
    background:
      linear-gradient(90deg, var(--lc-blue-soft, rgba(0,0,205,0.08)), transparent 72%),
      rgba(255,255,255,0.58);
    padding: 0.95rem 1rem;
    margin-bottom: 1.15rem;
  }

  html[data-theme="dark"] .lc-legal-alert {
    background:
      linear-gradient(90deg, rgba(184,199,255,0.10), transparent 72%),
      rgba(255,255,255,0.035);
  }

  .lc-legal-alert strong {
    display: block;
    color: var(--lc-blue, #0000CD);
    font-size: 0.82rem;
    line-height: 1;
    font-weight: 950;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
  }

  .lc-legal-alert p {
    margin: 0;
    color: var(--lc-muted, #667085);
    font-size: 0.92rem;
    line-height: 1.58;
    font-weight: 650;
  }

  .lc-legal-section {
    display: grid;
    grid-template-columns: 3.2rem minmax(0, 1fr);
    gap: 0.9rem;
    border-top: 1px solid var(--lc-border, rgba(0,0,205,0.14));
    padding-top: 1.05rem;
    margin-top: 1.05rem;
  }

  .lc-legal-number {
    display: inline-grid;
    place-items: center;
    width: 2.35rem;
    height: 2.35rem;
    border-radius: 0.85rem;
    background: var(--lc-blue, #0000CD);
    color: #fff;
    font-size: 0.82rem;
    line-height: 1;
    font-weight: 950;
    box-shadow: 0 12px 28px rgba(0,0,205,0.18);
  }

  html[data-theme="dark"] .lc-legal-number {
    color: #10131a;
    box-shadow: 0 12px 28px rgba(184,199,255,0.12);
  }

  .lc-legal-section h2 {
    margin: 0 0 0.45rem;
    color: var(--lc-heading, #242a32);
    font-size: clamp(1.08rem, 1.65vw, 1.3rem);
    line-height: 1.18;
    letter-spacing: -0.035em;
    font-weight: 950;
  }

  .lc-legal-section p {
    margin: 0;
    color: var(--lc-muted, #667085);
    font-size: 0.96rem;
    line-height: 1.7;
    font-weight: 620;
  }

  .lc-legal-section p + p {
    margin-top: 0.7rem;
  }

  .lc-legal-list {
    margin: 0.65rem 0 0;
    padding-left: 1.15rem;
    color: var(--lc-muted, #667085);
    font-size: 0.95rem;
    line-height: 1.65;
    font-weight: 620;
  }

  .lc-legal-list li + li {
    margin-top: 0.28rem;
  }

  .lc-legal-contact {
    margin-top: 1.25rem;
    border: 1px solid var(--lc-border, rgba(0,0,205,0.14));
    border-radius: 22px;
    background: rgba(255,255,255,0.58);
    padding: 1rem;
  }

  html[data-theme="dark"] .lc-legal-contact {
    background: rgba(255,255,255,0.035);
  }

  .lc-legal-contact h2 {
    margin: 0;
    color: var(--lc-heading, #242a32);
    font-size: 1.18rem;
    line-height: 1.18;
    letter-spacing: -0.035em;
    font-weight: 950;
  }

  .lc-legal-contact p {
    margin: 0.5rem 0 0;
    color: var(--lc-muted, #667085);
    font-size: 0.94rem;
    line-height: 1.55;
  }

  .lc-legal-contact a {
    display: inline-flex;
    margin-top: 0.7rem;
    border: 1px solid var(--lc-border-strong, rgba(0,0,205,0.24));
    border-radius: 999px;
    background: var(--lc-blue, #0000CD);
    color: #fff !important;
    padding: 0.62rem 0.9rem;
    font-size: 0.86rem;
    line-height: 1;
    font-weight: 900;
    text-decoration: none !important;
    box-shadow: 0 12px 30px rgba(0,0,205,0.18);
  }

  html[data-theme="dark"] .lc-legal-contact a {
    color: #10131a !important;
    box-shadow: 0 12px 30px rgba(184,199,255,0.12);
  }

  .lc-legal-footer-note {
    margin-top: 1rem;
    color: var(--lc-muted, #667085);
    font-size: 0.78rem;
    line-height: 1.55;
    font-weight: 620;
  }

  @media (max-width: 640px) {
    .lc-notice-page {
      width: min(100%, calc(100vw - 1rem));
    }

    .lc-legal-document {
      border-radius: 22px;
    }

    .lc-legal-section {
      grid-template-columns: 1fr;
      gap: 0.65rem;
    }
  }
</style>

<div class="lc-notice-page">
  <article class="lc-legal-document" aria-labelledby="ip-notice-title">
    <header class="lc-legal-header">
      <span class="lc-legal-kicker">Legal notice</span>
      <h1 class="lc-legal-title" id="ip-notice-title">Intellectual Property Notice</h1>
      <div class="lc-legal-meta">
        <span>Owner: Dr Kuan-Cheng (Louis) Chen</span>
        <span>Effective: 2026</span>
        <span>Website: louisanity.github.io</span>
      </div>
    </header>

    <section class="lc-legal-alert" aria-label="Summary notice">
      <strong>Summary</strong>
      <p>This notice distinguishes original research content, graphics, and custom visual design from the upstream open-source website framework.</p>
    </section>

    <section class="lc-legal-section">
      <div class="lc-legal-number">01</div>
      <div>
        <h2>Ownership of original materials</h2>
        <p>
          This website is maintained by <strong>Dr Kuan-Cheng (Louis) Chen</strong>. Unless otherwise stated, the original research descriptions, text, figures, diagrams, visual identity, custom layout decisions, and custom website design elements are © Kuan-Cheng (Louis) Chen.
        </p>
      </div>
    </section>

    <section class="lc-legal-section">
      <div class="lc-legal-number">02</div>
      <div>
        <h2>Reserved rights</h2>
        <p>
          Reuse, redistribution, republication, reproduction, adaptation, or derivative use of original materials from this website requires prior written permission.
        </p>
        <ul class="lc-legal-list">
          <li>Original research summaries and descriptions</li>
          <li>Figures, diagrams, visual banners, and graphical abstracts</li>
          <li>Custom page composition, visual identity, and presentation design</li>
          <li>Non-template text, images, and authored academic content</li>
        </ul>
      </div>
    </section>

    <section class="lc-legal-section">
      <div class="lc-legal-number">03</div>
      <div>
        <h2>Open-source framework distinction</h2>
        <p>
          This website is built using Jekyll and the AcademicPages / Minimal Mistakes ecosystem. Upstream template and theme code remains subject to its original open-source license and attribution requirements.
        </p>
        <p>
          This notice clarifies that the personal research content, custom graphics, and custom visual presentation are not offered for unrestricted reuse merely because the source repository is publicly visible.
        </p>
      </div>
    </section>

    <section class="lc-legal-section">
      <div class="lc-legal-number">04</div>
      <div>
        <h2>Requests for reuse</h2>
        <p>
          Requests to reuse, reproduce, adapt, or republish original materials should be made in writing and should identify the specific material, intended use, distribution channel, and attribution format.
        </p>
      </div>
    </section>

    <section class="lc-legal-contact" aria-label="Reuse contact">
      <h2>Contact</h2>
      <p>For reuse requests, collaboration enquiries, or permissions, please contact:</p>
      <a href="mailto:kuan-cheng.chen17@imperial.ac.uk">kuan-cheng.chen17@imperial.ac.uk</a>
    </section>

    <p class="lc-legal-footer-note">
      This notice is provided for website communication and rights clarification. It is not a substitute for jurisdiction-specific legal advice.
    </p>
  </article>
</div>
