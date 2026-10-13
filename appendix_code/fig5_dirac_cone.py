# ==============================================================================
# Appendix Fig. 1 -> fig5_dirac_cone.png
# Schematic of a Graphene Dirac Cone (3D surface plot)
# Extracted from: "15.09.2025 (STAJ-S1) Research Paper Prepared for the
# Internship - C. Zafer OSMANAGAOGLU" - Appendices section
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

kx = np.linspace(-2, 2, 100)
ky = np.linspace(-2, 2, 100)
KX, KY = np.meshgrid(kx, ky)

K_radius = np.sqrt(KX**2 + KY**2)
E_conduction = K_radius
E_valence = -K_radius

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(KX, KY, E_conduction, cmap='Reds', alpha=0.7, rstride=1,
                cstride=1)
ax.plot_surface(KX, KY, E_valence, cmap='Blues', alpha=0.7, rstride=1,
                cstride=1)
ax.scatter([0], [0], [0], color='black', s=100, label='Dirac Point (E=0)')

ax.set_xlabel('$k_x$ (Momentum)')
ax.set_ylabel('$k_y$ (Momentum)')
ax.set_zlabel('Energy (E)')
ax.set_title('Schematic of a Graphene Dirac Cone', fontsize=16)
ax.set_zlim([-2, 2])
ax.view_init(elev=20, azim=-65)
ax.legend()

plt.savefig("fig5_dirac_cone.png", dpi=300)
plt.show()
