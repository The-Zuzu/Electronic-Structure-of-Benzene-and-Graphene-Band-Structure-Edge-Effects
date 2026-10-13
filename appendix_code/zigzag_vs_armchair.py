# ==============================================================================
# Appendix Fig. 7 -> zigzag_vs_armchair_comparison.png
# Comparison of zigzag and armchair graphene flakes: structures + spectra
# Extracted from: "15.09.2025 (STAJ-S1) Research Paper Prepared for the
# Internship - C. Zafer OSMANAGAOGLU" - Appendices section
# NOTE (fix): In the paper the figure was saved to the author's Desktop; here it
# is saved to the current working directory so the script is portable.
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh
from collections import deque

# ==== NEW: Energy window around Fermi level (±EWIN) ====
EWIN = 1.8  # adjust as needed (e.g., 0.10, 0.20, ...)

# === ZIGZAG HEXAGONAL FLAKE ===
def create_zigzag_hexagonal_flake(n_rings):
    """
    Creates a hexagonal graphene flake with zigzag edges.
    """
    if n_rings == 0:
        return np.array([])
    a_cc = 1.0
    atom_positions = set()
    for i in range(-n_rings + 1, n_rings):
        for j in range(-n_rings + 1, n_rings):
            if abs(i+j) > n_rings-1:
                continue
            center = i * np.array([1.5, -np.sqrt(3)/2]) + j * np.array([1.5, np.sqrt(3)/2])
            for k in range(6):
                angle = np.pi / 3 * k
                x = center[0] + a_cc * np.cos(angle)
                y = center[1] + a_cc * np.sin(angle)
                atom_positions.add((round(x, 5), round(y, 5)))
    return np.array(list(atom_positions))

# === ARMCHAIR HEXAGONAL FLAKE ===
def create_armchair_hexagonal_flake(n_rings):
    """
    Creates a hexagonal graphene flake with armchair edges.
    """
    if n_rings == 0:
        return np.array([])
    a_cc = 1.0
    atom_positions = set()
    # Different center arrangement for armchair
    for i in range(-n_rings, n_rings + 1):
        for j in range(-n_rings, n_rings + 1):
            if abs(i + j) > n_rings:
                continue
            # Armchair centers
            center = i * np.array([3.0, 0.0]) + j * np.array([1.5, 1.5*np.sqrt(3)])
            # Add 6 atoms per center
            for k in range(6):
                angle = np.pi / 3 * k
                x = center[0] + a_cc * np.cos(angle)
                y = center[1] + a_cc * np.sin(angle)
                atom_positions.add((round(x, 5), round(y, 5)))
    return np.array(list(atom_positions))

# === GENERAL HAMILTONIAN AND SUB-LATTICE ASSIGNMENT ===
def assign_sublattices_and_build_hamiltonian(positions, t=2.7):
    """
    Assigns A/B sub-lattices and builds the Hamiltonian matrix.
    """
    n_atoms = len(positions)
    adj = [[] for _ in range(n_atoms)]
    for i in range(n_atoms):
        for j in range(i + 1, n_atoms):
            if np.isclose(np.linalg.norm(positions[i] - positions[j]), 1.0, atol=1e-3):
                adj[i].append(j)
                adj[j].append(i)

    sublattices = -np.ones(n_atoms, dtype=int)
    if n_atoms > 0:
        queue = deque([0])
        sublattices[0] = 0
        head = 0
        while head < len(queue):
            u = queue[head]; head += 1
            for v in adj[u]:
                if sublattices[v] == -1:
                    sublattices[v] = 1 - sublattices[u]
                    queue.append(v)

    H = lil_matrix((n_atoms, n_atoms), dtype=np.float64)
    for i in range(n_atoms):
        for j in adj[i]:
            if i < j:
                H[i, j] = -t
                H[j, i] = -t

    final_positions = np.hstack([positions, sublattices[:, np.newaxis]]) \
        if n_atoms > 0 else np.empty((0, 3))
    return H.tocsr(), final_positions

def calculate_flake_spectrum(H, num_eigenvalues):
    """Calculates the discrete energy spectrum of the finite flake."""
    n = H.shape[0]
    if n <= 1:
        return np.array([])
    k = min(num_eigenvalues, n - 2)
    if k <= 0:
        return np.sort(np.linalg.eigvalsh(H.toarray()))
    else:
        energies, _ = eigsh(H, k=k, which='SM', sigma=0)
        return np.sort(energies)

# === PLOTTING FUNCTION ===
def plot_comparison():
    """
    Compare zigzag (n_rings=3) and armchair (n_rings=2) structures + spectra.
    """
    # === ZIGZAG (n_rings = 3) ===
    n_rings_zigzag = 4
    zigzag_positions = create_zigzag_hexagonal_flake(n_rings_zigzag)
    H_zigzag, zigzag_flake = assign_sublattices_and_build_hamiltonian(zigzag_positions)
    zigzag_energies = calculate_flake_spectrum(H_zigzag, min(len(zigzag_positions), 200))

    # === ARMCHAIR (n_rings = 2) ===
    n_rings_armchair = 2
    armchair_positions = create_armchair_hexagonal_flake(n_rings_armchair)
    H_armchair, armchair_flake = assign_sublattices_and_build_hamiltonian(armchair_positions)
    armchair_energies = calculate_flake_spectrum(H_armchair, min(len(armchair_positions), 200))

    print(f"Zigzag: {len(zigzag_flake)} atoms")
    print(f"Armchair: {len(armchair_flake)} atoms")

    # === PLOT ===
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(f'Graphene Flakes Comparison\nZigzag vs Armchair',
                 fontsize=16, fontweight='bold')

    # === Row 1: Zigzag ===
    # Left: Structure
    ax1 = axes[0, 0]
    if len(zigzag_flake) > 0:
        ax1.scatter(zigzag_flake[:, 0], zigzag_flake[:, 1],
                    c=['#ff4d4d' if s == 0 else '#4d4dff' for s in zigzag_flake[:, 2]],
                    s=40, edgecolors='black', linewidth=0.5)
        for i in range(len(zigzag_flake)):
            for j in range(i+1, len(zigzag_flake)):
                if np.isclose(np.linalg.norm(zigzag_flake[i, :2] - zigzag_flake[j, :2]),
                              1.0, atol=1e-3):
                    ax1.plot(*zip(zigzag_flake[i, :2], zigzag_flake[j, :2]),
                             color='gray', linewidth=0.8)
        ax1.set_title(f'Zigzag Structure ({len(zigzag_flake)} atoms)')
        ax1.set_aspect('equal')
        ax1.grid(False)
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')

    # Right: Spectrum
    ax2 = axes[0, 1]
    if len(zigzag_energies) > 0:
        mask = np.abs(zigzag_energies) <= EWIN
        if np.any(mask):
            eigs_win = zigzag_energies[mask]
            idx_win = np.flatnonzero(mask)
            ax2.scatter(idx_win, eigs_win, c='red', s=30, marker='s',
                        alpha=0.8, label='Zigzag')
        else:
            ax2.text(0.5, 0.5, 'No states in window', transform=ax2.transAxes,
                     ha='center', va='center')
    ax2.axhline(0, color='blue', linestyle='--', linewidth=1.5, label='Fermi Level')
    ax2.set_title(f'Zigzag Energy Spectrum')
    ax2.set_xlabel('Eigenstate Index')
    ax2.set_ylabel('Energy [t]')
    ax2.set_ylim(-EWIN, EWIN)
    ax2.set_yticks(np.linspace(-EWIN, EWIN, 5))
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # === Row 2: Armchair ===
    # Left: Structure
    ax3 = axes[1, 0]
    if len(armchair_flake) > 0:
        ax3.scatter(armchair_flake[:, 0], armchair_flake[:, 1],
                    c=['#ff4d4d' if s == 0 else '#4d4dff' for s in armchair_flake[:, 2]],
                    s=40, edgecolors='black', linewidth=0.5)
        for i in range(len(armchair_flake)):
            for j in range(i+1, len(armchair_flake)):
                if np.isclose(np.linalg.norm(armchair_flake[i, :2] - armchair_flake[j, :2]),
                              1.0, atol=1e-3):
                    ax3.plot(*zip(armchair_flake[i, :2], armchair_flake[j, :2]),
                             color='gray', linewidth=0.8)
        ax3.set_title(f'Armchair Structure ({len(armchair_flake)} atoms)')
        ax3.set_aspect('equal')
        ax3.grid(False)
        ax3.set_xlabel('x')
        ax3.set_ylabel('y')

    # Right: Spectrum
    ax4 = axes[1, 1]
    if len(armchair_energies) > 0:
        mask = np.abs(armchair_energies) <= EWIN
        if np.any(mask):
            eigs_win = armchair_energies[mask]
            idx_win = np.flatnonzero(mask)
            ax4.scatter(idx_win, eigs_win, c='green', s=30, marker='o',
                        alpha=0.8, label='Armchair')
        else:
            ax4.text(0.5, 0.5, 'No states in window', transform=ax4.transAxes,
                     ha='center', va='center')
    ax4.axhline(0, color='blue', linestyle='--', linewidth=1.5, label='Fermi Level')
    ax4.set_title(f'Armchair Energy Spectrum')
    ax4.set_xlabel('Eigenstate Index')
    ax4.set_ylabel('Energy [t]')
    ax4.set_ylim(-EWIN, EWIN)
    ax4.set_yticks(np.linspace(-EWIN, EWIN, 5))
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    # Save (fixed: original code saved to ~/Desktop; now saves locally)
    filename = "zigzag_vs_armchair_comparison.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved successfully: {filename}")
    plt.show()

if __name__ == "__main__":
    print("Creating and comparing zigzag and armchair graphene flakes...")
    plot_comparison()
