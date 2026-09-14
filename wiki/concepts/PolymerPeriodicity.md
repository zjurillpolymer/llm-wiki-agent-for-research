---
title: "Polymer Periodicity"
type: concept
tags: [polymer-science, representation-learning]
sources: [periodicity-aware-deep-learning-for-polymers]
last_updated: 2026-09-14
---

# Polymer Periodicity

Polymer periodicity is the repeated-unit structure that distinguishes macromolecules from ordinary small molecules. It affects how local motifs are arranged over a chain and how polymer-level properties emerge. PerioGT treats this periodicity as a prior, using multiple augmented repeating-unit views and a learned prompt so that the representation remains stable across changes in fragment length and arrangement.

## Connections

- [[PerioGT]] — Explicitly models this prior.
- [[PolymerGraph]] — Represents repeated-unit structure and polymer conditions.
- [[ContrastiveLearning]] — Uses augmented views to learn periodicity-aware invariance.
