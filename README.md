# Electronic-Structure-of-Benzene-and-Graphene-Band-Structure-Edge-Effects

Comparative analysis of benzene and graphene electronic structures using Tight-Binding model (Python). Visualizes molecular orbitals, Dirac cones, and edge effects (zigzag/armchair) in graphene flakes with NN/NNN interactions.

## 📌 Overview
This project employs a Tight-Binding (TB) model to simulate and compare the electronic properties of **Benzene ($C_6H_6$)** and **Graphene**. By incorporating both Nearest-Neighbour ($t$) and Next-Nearest-Neighbour ($t'$) interactions, the study demonstrates the evolution from discrete molecular orbitals to continuous band structures.

Key focuses include:
* **Benzene:** Visualization of $\pi$-molecular orbitals and energy spectrum.
* **Graphene:** Simulation of Dirac cones, density of states (DOS), and band dispersion.
* **Quantum Confinement:** Analysis of **Zigzag** vs. **Armchair** edge effects in graphene nanoflakes and their impact on conductivity (semi-metallic vs. semiconducting behavior).

## 📊 Key Visualizations

### 1. Evolution of Electronic Structure
*Comparison of Benzene's discrete levels vs. Graphene's continuous bands.*
![Combined Spectrum](figures/fig1_combined_spectrum.png)
*(Note: Please ensure you upload your generated figures to a `figures` folder in your repo)*

### 2. Dirac Cones in Graphene
*3D representation of the linear dispersion relation at the K-point.*
![Dirac Cone](figures/fig5_dirac_cone.png)

### 3. Edge Effects: Zigzag vs. Armchair
*Demonstration of how edge geometry dictates the electronic gap.*
![Zigzag vs Armchair](figures/zigzag_vs_armchair_comparison.png)

## 🛠️ Tech Stack & Methods
* **Language:** Python 3.11
* **Libraries:** `NumPy`, `Matplotlib`, `SciPy`
* **Physics Models:**
    * Tight-Binding Model (NN & NNN)
    * LCAO (Linear Combination of Atomic Orbitals)
    * Hamiltonian Matrix Construction

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed. You can install the required dependencies via pip:

```bash
pip install numpy matplotlib scipy
