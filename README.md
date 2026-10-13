# Electronic Structure of Benzene and Graphene: Band Structure & Edge Effects

Comparative analysis of benzene and graphene electronic structures using the Tight-Binding model (Python). Visualizes molecular orbitals, Dirac cones, density of states, and edge effects (zigzag/armchair) in graphene flakes with NN/NNN interactions.

> 📄 This repository accompanies the research paper **"15.09.2025 (STAJ-S1) Research Paper Prepared for the Internship – C. Zafer OSMANAĞAOĞLULU"** (see [`paper/`](paper/) folder). All figures below are reproduced from the **Appendices** section of the paper.

## 📌 Overview
This project employs a Tight-Binding (TB) model to simulate and compare the electronic properties of **Benzene (C₆H₆)** and **Graphene**. By incorporating both Nearest-Neighbour (*t*) and Next-Nearest-Neighbour (*t′*) interactions, the study demonstrates the evolution from discrete molecular orbitals to continuous band structures.

Key focuses include:
* **Benzene:** Visualization of π-molecular orbitals, energy spectrum, and DOS.
* **Graphene:** Simulation of Dirac cones, schematic band structures, and the crystal lattice.
* **Quantum Confinement & Edge Effects:** Analysis of **Zigzag** vs. **Armchair** edges in graphene nanoflakes and the width–band-gap relationship (three-family *N = 3m, 3m+1, 3m+2* behavior per Han et al., 2007).

## 🗂️ Repository Structure

```
├── appendix_code/               # Python scripts extracted from the paper's Appendices
│   ├── fig5_dirac_cone.py       # Fig. 1 – 3D Dirac cone (linear dispersion)
│   ├── band_structures.py       # Fig. 2 – Schematic bands: metal / semiconductor / insulator / semi-metal
│   ├── benzene_tight_binding.py # Figs. 3–6 – Benzene TB spectrum, DOS, π-orbitals, graphene lattice
│   ├── zigzag_vs_armchair.py    # Fig. 7  – Zigzag vs armchair flakes + energy spectra
│   └── size_gap_relationship.py # Fig. 8  – System size vs energy gap (width-modulo-3 families)
├── figures/                     # Generated output images (PNG, 300 dpi)
├── paper/                       # Original research paper (PDF)
├── LICENSE
└── README.md
```

## 📊 Figures - Paper Appendix ↔ Code Mapping (all 8)

| Paper Fig. | Description | Script | Output Image |
|:---:|---|---|---|
| **Fig. 1** | Schematic graphene Dirac cone (3D linear dispersion at the K-point, E = 0) | [`appendix_code/fig5_dirac_cone.py`](appendix_code/fig5_dirac_cone.py) | `fig5_dirac_cone.png` |
| **Fig. 2** | Schematic band structures: Metal, Semiconductor, Insulator, Semi-metal (Graphene) | [`appendix_code/band_structures.py`](appendix_code/band_structures.py) | `band_structures.png` |
| **Fig. 3** | Benzene energy-level spectrum - NN vs. NNN tight-binding models | [`appendix_code/benzene_tight_binding.py`](appendix_code/benzene_tight_binding.py) | `fig1_combined_spectrum.png` |
| **Fig. 4** | Normalized Density of States (DOS), NN vs. NNN (Gaussian broadening) | [`appendix_code/benzene_tight_binding.py`](appendix_code/benzene_tight_binding.py) | `fig2_combined_dos.png` |
| **Fig. 5** | Benzene π molecular orbital probability densities (LCAO, individual + cumulative) | [`appendix_code/benzene_tight_binding.py`](appendix_code/benzene_tight_binding.py) | `fig3_benzene_orbitals.png` |
| **Fig. 6** | Graphene honeycomb crystal lattice (sublattices A/B, 20×20) | [`appendix_code/benzene_tight_binding.py`](appendix_code/benzene_tight_binding.py) | `fig4_graphene_lattice.png` |
| **Fig. 7** | Zigzag vs. Armchair graphene flakes - atomic structure + eigenvalue spectra near E_F | [`appendix_code/zigzag_vs_armchair.py`](appendix_code/zigzag_vs_armchair.py) | `zigzag_vs_armchair_comparison.png` |
| **Fig. 8** | Relationship between system size (ribbon width) and energy gap; three families (3m, 3m+1, 3m+2) | [`appendix_code/size_gap_relationship.py`](appendix_code/size_gap_relationship.py) | `fig8_size_gap_relationship.png` |

## 🖼️ Key Visualizations

### Fig. 1 - Dirac Cone in Graphene
*Linear dispersion relation at the K-point; conduction (π*) and valence (π) bands meet at E = 0.*
![Dirac Cone](figures/fig5_dirac_cone.png)

### Fig. 2 - Schematic Band Structures
*Comparison of metal, semiconductor, insulator, and semi-metal (graphene) band pictures with respect to the Fermi level.*
![Band Structures](figures/band_structures.png)

### Fig. 3 - Benzene Energy Levels (NN vs. NNN)
*Discrete π levels of the 6-site ring; NNN hopping (t′ = 0.1|t|) lifts the degeneracies.*
![Combined Spectrum](figures/fig1_combined_spectrum.png)

### Fig. 4 - Density of States
*Normalized DOS for the NN and NNN benzene models (vertically stacked panels).*
![Combined DOS](figures/fig2_combined_dos.png)

### Fig. 5 - Benzene π Molecular Orbitals
*LCAO probability densities: individual states (top row) and cumulative filling up to the Fermi level (bottom row).*
![Benzene Orbitals](figures/fig3_benzene_orbitals.png)

### Fig. 6 - Graphene Crystal Lattice
*Honeycomb lattice with two sublattices (A: blue, B: red) built from lattice vectors a₁, a₂.*
![Graphene Lattice](figures/fig4_graphene_lattice.png)

### Fig. 7 - Edge Effects: Zigzag vs. Armchair
*Hexagonal flakes with zigzag (edge-state flat band near E_F) and armchair (finite gap) terminations, with their sparse-eigensolver spectra.*
![Zigzag vs Armchair](figures/zigzag_vs_armchair_comparison.png)

### Fig. 8 - Size–Gap Relationship
*E_gap ∝ 1/W for armchair ribbons with three distinct width-modulo-3 families; zigzag remains gapless (after Han et al., 2007).*
![Size Gap Relationship](figures/fig8_size_gap_relationship.png)

## 🛠️ Tech Stack & Methods
* **Language:** Python 3.11
* **Libraries:** `NumPy`, `Matplotlib`, `SciPy` (`scipy.sparse` + `eigsh` for large flake Hamiltonians)
* **Physics Models:**
    * Tight-Binding Model (NN *t* = −2.7 eV & NNN *t′* ≈ 0.1|t|)
    * LCAO (Linear Combination of Atomic Orbitals)
    * Hamiltonian Matrix Construction & Diagonalization
    * Sub-lattice BFS assignment for bipartite flakes
    * Quantum confinement / edge-state physics (Fermi-window spectroscopy)

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy matplotlib scipy
```

### Running the simulations
Each script is self-contained; run it from the `appendix_code/` directory and the PNG is written to the current working directory:

```bash
cd appendix_code
python fig5_dirac_cone.py        # Fig. 1
python band_structures.py        # Fig. 2
python benzene_tight_binding.py  # Figs. 3, 4, 5, 6
python zigzag_vs_armchair.py     # Fig. 7
python size_gap_relationship.py  # Fig. 8
```

Regenerated images can be moved into `figures/` to update this README's previews.

## 📄 License
Distributed under the MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author
**C. Zafer OSMANAĞAOĞLULU** - Internship Research Project (STAJ-S1), September 2025.
