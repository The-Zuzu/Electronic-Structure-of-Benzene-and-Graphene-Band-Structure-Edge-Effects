# ==============================================================================
# Appendix Fig. 2 -> schematic band structures
# Metal, Semiconductor, Insulator and Semi-Metal (Graphene) compared side by side
# Extracted from: "15.09.2025 (STAJ-S1) Research Paper Prepared for the
# Internship - C. Zafer OSMANAGAOGLU" - Appendices section
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt

# Create a figure with 4 subplots
fig, axes = plt.subplots(1, 4, figsize=(18, 6))
fig.suptitle('Schematic Band Structures: Metal, Semiconductor, '
             'Insulator, Semi-Metal (Graphene)', fontsize=16)

# Define common parameters
k = np.linspace(-1, 1, 200)
fermi_level = 0  # Fermi level at E=0

# ========================================================================
# 1. METAL
# ========================================================================
ax = axes[0]
ax.fill_between(k, -1.5, fermi_level, color='lightblue', alpha=0.8,
                label='Valence Band')
ax.fill_between(k, fermi_level, 1.5, color='lightcoral', alpha=0.8,
                label='Conduction Band')
ax.axhline(y=fermi_level, color='black', linestyle='--', linewidth=2,
           label='Fermi Level (E_F)')
ax.set_title('Metal', fontweight='bold')
ax.set_xlabel('k (Momentum)')
ax.set_ylabel('Energy (E)')
ax.set_ylim(-2, 2)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# ========================================================================
# 2. SEMICONDUCTOR
# ========================================================================
ax = axes[1]
valence_band_semi = -0.5 - 0.3 * np.cos(np.pi * k)
conduction_band_semi = 0.5 + 0.3 * np.cos(np.pi * k)
ax.plot(k, valence_band_semi, color='blue', linewidth=3, label='Valence Band')
ax.plot(k, conduction_band_semi, color='red', linewidth=3,
        label='Conduction Band')
ax.axhline(y=fermi_level, color='black', linestyle='--', linewidth=2,
           label='Fermi Level (E_F)')
ax.fill_between(k, valence_band_semi, conduction_band_semi,
                where=(conduction_band_semi > valence_band_semi),
                color='gray', alpha=0.2, label='Band Gap')
ax.set_title('Semiconductor', fontweight='bold')
ax.set_xlabel('k (Momentum)')
ax.set_ylabel('Energy (E)')
ax.set_ylim(-2, 2)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# ========================================================================
# 3. INSULATOR
# ========================================================================
ax = axes[2]
valence_band_ins = -1.0 - 0.3 * np.cos(np.pi * k)
conduction_band_ins = 1.0 + 0.3 * np.cos(np.pi * k)
ax.plot(k, valence_band_ins, color='blue', linewidth=3, label='Valence Band')
ax.plot(k, conduction_band_ins, color='red', linewidth=3,
        label='Conduction Band')
ax.axhline(y=fermi_level, color='black', linestyle='--', linewidth=2,
           label='Fermi Level (E_F)')
ax.fill_between(k, valence_band_ins, conduction_band_ins,
                where=(conduction_band_ins > valence_band_ins),
                color='gray', alpha=0.2, label='Large Band Gap')
ax.set_title('Insulator', fontweight='bold')
ax.set_xlabel('k (Momentum)')
ax.set_ylabel('Energy (E)')
ax.set_ylim(-2, 2)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# ========================================================================
# 4. SEMI-METAL (GRAPHENE)
# ========================================================================
ax = axes[3]
dirac_cone_positive = 1.5 * np.abs(k)  # Conduction band
dirac_cone_negative = -1.5 * np.abs(k)  # Valence band
ax.plot(k, dirac_cone_positive, color='red', linewidth=3,
        label='Conduction Band')
ax.plot(k, dirac_cone_negative, color='blue', linewidth=3,
        label='Valence Band')
ax.axhline(y=fermi_level, color='black', linestyle='--', linewidth=2,
           label='Fermi Level (E_F)')
ax.plot(0, 0, 'ko', markersize=8, label='Dirac Point')
ax.set_title('Semi-Metal (Graphene)', fontweight='bold')
ax.set_xlabel('k (Momentum)')
ax.set_ylabel('Energy (E)')
ax.set_ylim(-2, 2)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# ========================================================================
# Display and save the plot
# ========================================================================
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("band_structures.png", dpi=300)
plt.show()
