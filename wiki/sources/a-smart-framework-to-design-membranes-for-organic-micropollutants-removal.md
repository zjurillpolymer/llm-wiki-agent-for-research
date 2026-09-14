---
title: "A smart framework to design membranes for organic micropollutants removal"
type: source
tags: [membranes, water-treatment, machine-learning, mechanism]
sources: []
last_updated: 2026-09-14
date: 2025-08-25
source_file: s41893-025-01617-6.pdf
---

## Summary

This paper presents a data-mechanism-fused molecular representation learning model, [[DMF-MRL]], for understanding and designing polymeric membranes that remove organic micropollutants (OMPs). The model combines molecular fingerprints with physical descriptions from [[XDLVO]] and [[DSPM-DE]], together with multilevel molecular and membrane descriptors. The authors use the model to show that OMP rejection depends on context-dependent functional-group coupling rather than on isolated functional groups alone, and then construct an interaction framework for tailoring [[PolyamideMembranes]].

## Key Claims

- The dataset contains 2,102 entries covering 277 OMPs, 52 membrane types and 40 descriptions. Among four tested algorithms, XGBoost performed best, with a test R2 of 0.881 after optimization and fivefold cross-validation.
- DMF-MRL outperforms a data-only model without molecular fingerprints and physical-model features, while retaining interpretable feature contributions through SHAP and partial-dependence analyses.
- Functional-group importance changes when groups are connected to other substructures. In particular, phenyl-containing structures show multigroup coupling in which hydrophobic interaction, molecular size resistance and pi-pi interactions jointly influence rejection.
- The effect of increasing phenyl-group count is non-monotonic: stronger membrane interaction can reduce rejection, while the simultaneous increase in molecular size can increase size-sieving resistance.
- The dominant rejection factors differ across membrane and OMP classes. Hydrophobic interaction is especially important for phenyl-hydrophobic OMPs in nanofiltration, size sieving is important for phenyl-hydrophilic OMPs, and Donnan exclusion is important for phenyl-charged OMPs.
- The proposed design framework uses surface-charge inversion, zwitterionization, charge enhancement, hydrophilicity and pore architecture to tailor membranes for different OMP classes.

## Key Quotes

> The efficiency of removal depends on the influence of functional-group coupling in the molecular structure.

> The data-mechanism co-driven paradigm has the potential to facilitate the development of advanced water-treatment membranes.

## Connections

- [[DanLu]] — First author and contributor to the membrane design study.
- [[ZhejiangUniversity]] — The study includes researchers from Zhejiang University.
- [[OrganicMicropollutants]] — Target contaminants whose rejection is modeled.
- [[DMF-MRL]] — Main model proposed by the paper.
- [[XDLVO]] — Physical model embedded to represent solute-membrane interaction energy.
- [[DSPM-DE]] — Physical model embedded to represent size sieving and Donnan/dielectric exclusion.
- [[PolyamideMembranes]] — Main membrane family studied and modified experimentally.
- [[PerioGT]] — Related work in this collection that also embeds polymer-domain knowledge into ML.

## Contradictions

- No direct contradiction with the current wiki. The paper qualifies simple rules based on isolated functional groups by showing that molecular context can reverse or change their apparent effect.

## Source Metadata

- DOI: 10.1038/s41893-025-01617-6
- Journal: Nature Sustainability
- Publication date: 25 August 2025
- Authors: Dan Lu, Zihang Zhao, Xinchen Xiang, Tianyu Li, Yifang Geng, Ming Wu, Yangyang Li, Shiying Xu, Chuanqi Zhang, Zhuofan Gao, Jia-Wei Shen, Lijun Liang, Kai Fan, Zhikan Yao and Lin Zhang.
