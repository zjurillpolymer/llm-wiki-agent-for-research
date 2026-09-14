---
title: "Overview"
type: synthesis
tags: []
sources: []
last_updated: "2026-09-14"
---

# Overview

The current collection focuses on machine learning for polymer and membrane science. The two papers share a data-driven materials design perspective, but operate at different levels: [[DMF-MRL]] combines molecular fingerprints with physical models to explain organic micropollutant rejection by [[PolyamideMembranes]], whereas [[PerioGT]] builds a polymer representation that explicitly preserves [[PolymerPeriodicity]].

The membrane study shows that rejection cannot always be explained by isolated functional groups. Molecular context and multigroup coupling can change the direction and importance of a group-level effect, so membrane design needs to account for hydrophobic interaction, size sieving, Donnan exclusion and operating conditions together. The polymer study makes a parallel representation-learning argument: polymer structures should not be treated as ordinary small-molecule graphs, because repeated units and polymer-level conditions carry essential information.

Together, the papers support a common research pattern: encode domain knowledge into machine-learning representations, use interpretable analyses to connect predictions to mechanisms, and validate the resulting design rules with experiments. The current evidence covers water-treatment membranes, polymer property prediction and antimicrobial polymer discovery; it does not yet cover molecular dynamics as a primary design loop or compare the two model families on a shared dataset.
