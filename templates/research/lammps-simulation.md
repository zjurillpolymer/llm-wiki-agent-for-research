---
title: "LAMMPS Simulation: YYYY-MM-DD | system"
type: source
tags: [simulation, lammps, molecular-dynamics]
date: YYYY-MM-DD
source_file: raw/simulations/...
project: "Project name"
simulation_id: "MD-YYYY-MM-DD-01"
---

## Objective

What physical or chemical question is being tested?

## System Definition

- Components and composition:
- Number of atoms or molecules:
- Initial configuration:
- Box dimensions and boundary conditions:
- Temperature and pressure:

## Model and Parameters

- Force field or potential:
- Pair, bond, angle and dihedral styles:
- Charge model:
- Long-range solver:
- Reactive method, if any:
- Timestep:
- Equilibration and production length:
- Number of replicas and random seeds:

## Workflow

Describe minimization, equilibration, production, perturbations and restart
steps. Link the exact input and analysis scripts.

## Observables

- Quantities measured:
- Sampling interval:
- Analysis method:
- Uncertainty estimation:

## Results

Separate directly measured simulation outputs from interpretation. Link output
files, plots and important frames.

## Reproducibility

- LAMMPS version:
- Hardware and parallel settings:
- Input files:
- Analysis scripts:
- Checksum or commit:

## Limitations

Finite-size effects, force-field assumptions, timescale limits, convergence
issues and any missing control simulations.

## Connections

- [[ProjectName]] — project context
- [[PaperName]] — source of the hypothesis or parameters
- [[AnalysisScript]] — analysis workflow
