---
title: "PolymerGraph"
type: concept
tags: [graph-learning, polymer-informatics]
sources: [periodicity-aware-deep-learning-for-polymers]
last_updated: 2026-09-14
---

# PolymerGraph

PolymerGraph is the graph representation used by PerioGT. Polymer repeating units are converted from SMILES into graphs, and virtual nodes connect components or carry sample-level conditions such as copolymer type and molecular weight. This design lets the graph encoder preserve local chemical structure while also communicating global polymer and experimental context.

## Connections

- [[PerioGT]] — Main model using PolymerGraph.
- [[PolymerPeriodicity]] — Repeated-unit structure motivates the representation.
- [[ContrastiveLearning]] — Augmented PolymerGraph views support pre-training.
