---
title: "DMF-MRL"
type: concept
tags: [machine-learning, interpretable-ml, membranes]
sources: [a-smart-framework-to-design-membranes-for-organic-micropollutants-removal]
last_updated: 2026-09-14
---

# DMF-MRL

Data-mechanism-fused molecular representation learning (DMF-MRL) is the framework proposed for OMP-removal membrane design. It combines molecular fingerprints, multilevel feature descriptors and physical-model features from [[XDLVO]] and [[DSPM-DE]] inside a machine-learning model. The framework uses XGBoost as its selected predictor and applies SHAP, partial-dependence analysis and molecular-dynamics calculations to connect model output with molecular interaction mechanisms.

## Connections

- [[OrganicMicropollutants]] — Prediction target.
- [[XDLVO]] — Encodes solute-membrane interaction energy.
- [[DSPM-DE]] — Encodes pore and charge effects.
- [[PolyamideMembranes]] — Material platform for the design rules.
- [[PerioGT]] — Related domain-knowledge-guided representation-learning framework.
