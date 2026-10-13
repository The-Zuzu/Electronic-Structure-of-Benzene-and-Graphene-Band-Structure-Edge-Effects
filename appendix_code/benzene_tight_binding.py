# ==============================================================================
# Appendix "Fig. 3, Fig. 4, Fig. 5, Fig. 6" ->
#   fig1_combined_spectrum.png  (Appendix Fig. 3: Benzene energy level spectrum)
#   fig2_combined_dos.png       (Appendix Fig. 4: DOS, NN vs NNN)
#   fig3_benzene_orbitals.png   (Appendix Fig. 5: Benzene pi-orbital densities)
#   fig4_graphene_lattice.png   (Appendix Fig. 6: Graphene crystal lattice)
# Extracted from: "15.09.2025 (STAJ-S1) Research Paper Prepared for the
# Internship - C. Zafer OSMANAGAOGLU" - Appendices section
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# =============================================================================
# --- Main Parameters and Hamiltonians ---
# =============================================================================
N_ATOMS = 6
t = -2.7  # Nearest-neighbour (NN) hopping integral
t_prime = -0.1 * t  # Next-nearest-neighbour (NNN) hopping integral, t' ~ 0.1|t|

# NN Hamiltonian
H_nn = np.zeros((N_ATOMS, N_ATOMS))
for i in range(N_ATOMS):
    H_nn[i, (i + 1) % N_ATOMS] = t
    H_nn[i, (i - 1 + N_ATOMS) % N_ATOMS] = t

# NNN Hamiltonian
H_nnn = np.zeros((N_ATOMS, N_ATOMS))
for i in range(N_ATOMS):
    H_nnn[i, (i + 1) % N_ATOMS] = t
    H_nnn[i, (i - 1 + N_ATOMS) % N_ATOMS] = t
    H_nnn[i, (i + 2) % N_ATOMS] = t_prime
    H_nnn[i, (i - 2 + N_ATOMS) % N_ATOMS] = t_prime

# Calculate and sort eigenvalues for both models
eigenvalues_nn, _ = np.linalg.eigh(H_nn)
eigenvalues_nnn, _ = np.linalg.eigh(H_nnn)
eigenvalues_nn.sort()
eigenvalues_nnn.sort()

# =============================================================================
# --- FIGURE 1: Combined Energy Level Spectrum (NN vs. NNN) ---
# =============================================================================
def generate_combined_spectrum_plot(e_vals_nn, e_vals_nnn):
    """Plots the energy level spectra for both NN and NNN models on the same axes."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title("Benzene Energy Level Spectrum (NN vs. NNN)")
    ax.set_ylabel("Energy (E/|t|)")
    ax.set_xlabel("Energy Level Index")
    ax.set_xticks(range(N_ATOMS))
    ax.set_xticklabels([f'E{i+1}' for i in range(N_ATOMS)])

    # Plot NN eigenvalues
    for i, E in enumerate(e_vals_nn):
        ax.hlines(E, xmin=i - 0.4, xmax=i, colors='blue', linestyles='--')
        ax.plot(i - 0.2, E, 'bo', markersize=8, label='NN Model' if i == 0 else "")

    # Plot NNN eigenvalues
    for i, E in enumerate(e_vals_nnn):
        ax.hlines(E, xmin=i, xmax=i + 0.4, colors='red', linestyles=':')
        ax.plot(i + 0.2, E, 'r^', markersize=8,
                label="NNN Model (t' = 0.1|t|)" if i == 0 else "")

    ax.axhline(0, color='black', linestyle='-', linewidth=1.5,
               label='Fermi Level (E=0)')
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlim(-0.5, N_ATOMS - 0.5)
    plt.tight_layout()
    plt.savefig("fig1_combined_spectrum.png", dpi=300)
    plt.show()

# =============================================================================
# --- FIGURE 2: Combined Normalized Density of States (NN vs. NNN) -- ALT ALTA ---
# =============================================================================
def generate_combined_dos_plot(e_vals_nn, e_vals_nnn):
    """Plots the normalized DOS for NN and NNN models in two subplots (vertically stacked)."""
    sigma = 0.08  # Gaussian broadening
    spin_deg = 2

    E_min = min(e_vals_nn.min(), e_vals_nnn.min()) - 5 * sigma
    E_max = max(e_vals_nn.max(), e_vals_nnn.max()) + 5 * sigma
    E_grid = np.linspace(E_min, E_max, 1000)

    # Function to calculate DOS
    def calculate_dos(eigenvalues):
        dos = np.zeros_like(E_grid)
        A_norm = spin_deg / (np.sqrt(2 * np.pi) * sigma)
        for E_i in eigenvalues:
            dos += A_norm * np.exp(-(E_grid - E_i)**2 / (2 * sigma**2))
        return dos

    dos_nn = calculate_dos(e_vals_nn)
    dos_nnn = calculate_dos(e_vals_nnn)

    # Create subplots vertically
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle("Normalized Density of States (NN vs. NNN)", fontsize=16)

    # Top subplot: NN Model
    ax1.plot(E_grid, dos_nn, lw=2.5, color='blue', label='NN Model')
    ax1.fill_between(E_grid, dos_nn, color='blue', alpha=0.15)
    ax1.set_ylabel("Normalized DOS (1/|t|)")
    ax1.set_title("Nearest-Neighbor (NN) Model")
    ax1.legend()
    ax1.set_ylim(bottom=0)
    ax1.grid(True, linestyle=':', alpha=0.6)

    # Bottom subplot: NNN Model
    ax2.plot(E_grid, dos_nnn, lw=2.5, color='red', linestyle='--',
             label="NNN Model (t' = 0.1|t|)")
    ax2.fill_between(E_grid, dos_nnn, color='red', alpha=0.15)
    ax2.set_ylabel("Normalized DOS (1/|t|)")
    ax2.set_xlabel("Energy (E/|t|)")
    ax2.set_title("Next-Nearest-Neighbor (NNN) Model")
    ax2.legend()
    ax2.set_ylim(bottom=0)
    ax2.grid(True, linestyle=':', alpha=0.6)

    # Shared x-axis settings
    ax2.set_xlim(E_min, E_max)
    plt.tight_layout()
    plt.savefig("fig2_combined_dos.png", dpi=300)
    plt.show()

# =============================================================================
# --- FIGURE 3: Benzene Molecular Orbital Probability Densities ---
# =============================================================================
def generate_benzene_orbitals():
    """Visualizes the probability densities of benzene's pi-molecular orbitals."""
    GRID_SIZE = 400
    PLOT_LIMIT = 3.5
    BOND_LENGTH = 1.39  # Angstrom
    ATOMIC_ORBITAL_WIDTH = 0.7

    # LCAO coefficients, ordered by energy
    coefficients = np.array([
        [1,  1,  1,  1,  1,  1],
        [2,  1, -1, -2, -1,  1],
        [0,  1,  1,  0, -1, -1],
        [0,  1, -1,  0,  1, -1],
        [2, -1, -1,  2, -1, -1],
        [1, -1,  1, -1,  1, -1]
    ]) * (1 / np.sqrt([6, 12, 4, 4, 12, 6]))[:, np.newaxis]

    angles = np.linspace(0, 2 * np.pi, N_ATOMS, endpoint=False)
    atom_coords = np.c_[BOND_LENGTH * np.cos(angles), BOND_LENGTH * np.sin(angles)]

    x = np.linspace(-PLOT_LIMIT, PLOT_LIMIT, GRID_SIZE)
    y = np.linspace(-PLOT_LIMIT, PLOT_LIMIT, GRID_SIZE)
    X, Y = np.meshgrid(x, y)
    cell_area = (2 * PLOT_LIMIT / GRID_SIZE) ** 2

    atomic_orbitals = np.array([
        np.exp(-((X - ax)**2 + (Y - ay)**2) / (2 * ATOMIC_ORBITAL_WIDTH**2))
        for ax, ay in atom_coords
    ])
    for i in range(N_ATOMS):
        atomic_orbitals[i] /= np.sqrt(np.sum(atomic_orbitals[i]**2) * cell_area)

    molecular_orbitals = np.tensordot(coefficients, atomic_orbitals, axes=1)
    for i in range(N_ATOMS):
        molecular_orbitals[i] /= np.sqrt(np.sum(molecular_orbitals[i]**2) * cell_area)

    individual_densities = molecular_orbitals**2
    cumulative_densities = np.cumsum(individual_densities, axis=0)
    max_density = cumulative_densities[-1].max()
    individual_densities_scaled = individual_densities / max_density
    cumulative_densities_scaled = cumulative_densities / max_density

    fig, axes = plt.subplots(2, 6, figsize=(24, 9))
    fig.suptitle("Benzene π Molecular Orbitals (Normalized)\n"
                 "Individual & Cumulative Probability Densities", fontsize=20)

    for i in range(N_ATOMS):
        # Top Row: Individual Densities
        ax_ind = axes[0, i]
        ax_ind.imshow(individual_densities_scaled[i],
                      extent=[-PLOT_LIMIT, PLOT_LIMIT, -PLOT_LIMIT, PLOT_LIMIT],
                      origin='lower', cmap='viridis', vmin=0, vmax=1.0)
        ax_ind.set_title(f"State {i+1}")
        ax_ind.scatter(atom_coords[:, 0], atom_coords[:, 1], s=30, c='red', alpha=0.7)

        # Bottom Row: Cumulative Densities
        ax_cum = axes[1, i]
        ax_cum.imshow(cumulative_densities_scaled[i],
                      extent=[-PLOT_LIMIT, PLOT_LIMIT, -PLOT_LIMIT, PLOT_LIMIT],
                      origin='lower', cmap='viridis', vmin=0, vmax=1.0)
        ax_cum.set_title(f"States 1-{i+1}")
        ax_cum.scatter(atom_coords[:, 0], atom_coords[:, 1], s=30, c='red', alpha=0.7)

    for ax in axes.flat:
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout(rect=[0, 0, 0.95, 0.95])
    plt.savefig("fig3_benzene_orbitals.png", dpi=300)
    plt.show()

# =============================================================================
# --- FIGURE 4: Graphene Crystal Lattice ---
# =============================================================================
def generate_graphene_lattice(N=20, M=20):
    """Generates and plots a graphene crystal lattice."""
    a_cc = 1.42  # Angstrom
    a1 = a_cc * np.array([3/2, np.sqrt(3)/2])
    a2 = a_cc * np.array([3/2, -np.sqrt(3)/2])

    atoms_A = []
    atoms_B = []
    for n in range(N):
        for m in range(M):
            R = n * a1 + m * a2
            atoms_A.append(R)
            atoms_B.append(R + np.array([a_cc, 0]))
    atoms_A = np.array(atoms_A)
    atoms_B = np.array(atoms_B)
    all_atoms = np.vstack((atoms_A, atoms_B))

    bonds = []
    for i in range(len(all_atoms)):
        for j in range(i + 1, len(all_atoms)):
            if np.linalg.norm(all_atoms[i] - all_atoms[j]) < a_cc + 0.1:
                bonds.append([all_atoms[i], all_atoms[j]])

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.add_collection(LineCollection(bonds, colors='gray', linewidths=1.5, zorder=1))
    ax.scatter(atoms_A[:, 0], atoms_A[:, 1], s=50, c='blue', label='Sublattice A', zorder=2)
    ax.scatter(atoms_B[:, 0], atoms_B[:, 1], s=50, c='red', label='Sublattice B', zorder=2)
    ax.set_title(f'{N}x{M} Graphene Lattice', fontsize=16)
    ax.set_xlabel('X Coordinate (Å)')
    ax.set_ylabel('Y Coordinate (Å)')
    ax.set_aspect('equal', adjustable='box')
    ax.legend()
    plt.tight_layout()
    plt.savefig("fig4_graphene_lattice.png", dpi=300)
    plt.show()

# =============================================================================
# --- Generate All Figures ---
# =============================================================================
if __name__ == '__main__':
    print("Generating Figure 1: Energy Level Spectrum...")
    generate_combined_spectrum_plot(eigenvalues_nn, eigenvalues_nnn)
    print("Generating Figure 2: Density of States (NN and NNN, vertically stacked)...")
    generate_combined_dos_plot(eigenvalues_nn, eigenvalues_nnn)
    print("Generating Figure 3: Benzene Molecular Orbitals...")
    generate_benzene_orbitals()
    print("Generating Figure 4: Graphene Lattice...")
    generate_graphene_lattice()
