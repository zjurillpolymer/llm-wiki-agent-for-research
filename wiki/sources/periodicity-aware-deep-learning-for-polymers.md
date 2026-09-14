---
title: "Periodicity-aware deep learning for polymers"
type: source
tags: [polymers, deep-learning, graph-learning, self-supervised-learning]
sources: []
last_updated: 2026-09-14
date: 2025-11-20
source_file: s43588-025-00903-9.pdf
---

## Summary

This paper introduces [[PerioGT]], a periodicity-aware graph-transformer framework for polymer representation learning and property prediction. It treats the repeated-unit structure of polymers as a chemical prior and combines periodicity-aware augmentation, contrastive learning, masked node modeling, virtual nodes and learned periodicity prompts. PerioGT achieves strong performance across polymer prediction tasks and is applied to antimicrobial polymer discovery, where predictions are validated experimentally against methicillin-resistant Staphylococcus aureus (MRSA).

## Key Claims

- Polymer periodicity is a fundamental structural feature that is lost when polymers are simplified to isolated repeating units or ordinary small-molecule graphs.
- PerioGT pre-trains on approximately one million unlabeled virtual polymers. Its self-supervised objectives combine periodicity-aware contrastive learning with masked node modeling.
- Periodicity-aware augmentation generates multiple repeating-unit views of the same polymer. The model uses these views to learn representations that remain stable under changes in repeating-unit size, arrangement and minor atomic substitutions.
- The framework uses [[PolymerGraph]] representations with virtual nodes to connect copolymer components and incorporate sample-level conditions such as copolymer type and molecular weight.
- PerioGT outperforms the compared supervised and self-supervised baselines on the reported downstream tasks. In periodicity analysis, its average similarity between original repeating units and augmentations is 0.84, and its K-nearest-neighbor classification accuracy exceeds 80%, whereas the other self-supervised baselines remain below 40%.
- For antimicrobial polymer discovery, the authors generate 624 candidates from 12 diacrylates and 52 amines, synthesize and label 150 of them, and select the top 30 predicted candidates. PerioGT reaches an 83% screening success rate, compared with 57% for TransPolymer and 20% for polyBERT.
- Two lead polymers have a minimum inhibitory concentration of 8 micrograms per millilitre against MRSA. Follow-up assays show strong bacterial killing, membrane-potential disturbance and membrane disruption.

## Key Quotes

> Existing self-supervised learning methods simplify polymers into repeating units and neglect their inherent periodicity.

> Introducing the periodicity prior effectively enhances model performance.

## Connections

- [[YuhuiWu]] — First author and developer of the PerioGT framework.
- [[JianJi]] — Corresponding senior author and project supervisor.
- [[ZhejiangUniversity]] — The authors are affiliated with Zhejiang University.
- [[PerioGT]] — Main model proposed by the paper.
- [[PolymerPeriodicity]] — Domain prior encoded by the model.
- [[PolymerGraph]] — Graph construction used to represent polymer structures and conditions.
- [[ContrastiveLearning]] — One of the principal self-supervised objectives.
- [[DMF-MRL]] — Related work in this collection that also fuses domain knowledge with ML for polymer and membrane science.

## Contradictions

- No direct contradiction with the current wiki. Both current papers argue that domain-specific structure and mechanism should be represented explicitly rather than left entirely to generic molecular features.

## Source Metadata

- DOI: 10.1038/s43588-025-00903-9
- Journal: Nature Computational Science
- Publication date: 20 November 2025
- Authors: Yuhui Wu, Cong Wang, Xintian Shen, Tianyi Zhang, Peng Zhang and Jian Ji.
- Code: https://github.com/wuyuhui-zju/PerioGT
