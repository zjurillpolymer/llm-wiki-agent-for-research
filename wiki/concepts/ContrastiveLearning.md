---
title: "Contrastive Learning"
type: concept
tags: [self-supervised-learning, representation-learning]
sources: [periodicity-aware-deep-learning-for-polymers]
last_updated: 2026-09-14
---

# Contrastive Learning

Contrastive learning trains a representation so that related views are close and unrelated views are separated. In PerioGT, multiple periodicity-aware augmentations of a polymer act as related views. The contrastive objective encourages the model to preserve polymer identity and periodic structure despite changes in repeating-unit size, arrangement and small structural perturbations.

## Connections

- [[PerioGT]] — Uses periodicity-aware contrastive pre-training.
- [[PolymerPeriodicity]] — Defines the invariances the model should learn.
- [[PolymerGraph]] — Supplies graph views for the self-supervised objective.
