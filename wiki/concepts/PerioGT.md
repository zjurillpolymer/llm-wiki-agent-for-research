---
title: "PerioGT"
type: concept
tags: [deep-learning, graph-neural-network, polymer-informatics]
sources: [periodicity-aware-deep-learning-for-polymers]
last_updated: 2026-09-14
---

# PerioGT

PerioGT is a periodicity-aware graph-transformer framework for polymer representation learning. It combines [[PolymerGraph]] construction, periodicity-aware augmentation, contrastive learning, masked node modeling and learned periodicity prompts. The resulting representations are fine-tuned for polymer property prediction and candidate screening, including antimicrobial polymer discovery.

## Connections

- [[PolymerPeriodicity]] — Structural prior encoded by PerioGT.
- [[PolymerGraph]] — Graph representation used by the model.
- [[ContrastiveLearning]] — Self-supervised training objective.
- [[DMF-MRL]] — Another materials-ML framework that incorporates domain knowledge.
