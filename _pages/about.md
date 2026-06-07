# Homepage Bloch sphere no-label hotfix

This patch removes the visible Bloch-sphere text labels such as `|ψ⟩`, while keeping the clean sphere, rings, axes, and state-vector motif.

## Apply

```bash
unzip louisanity_homepage_bloch_no_labels_2026-06-07.zip -d .
git add _pages/about.md README_HOMEPAGE_BLOCH_NO_LABELS.md
git commit -m "Remove Bloch sphere text labels"
git push origin master
```
