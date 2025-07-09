import numpy as np
import matplotlib.pyplot as plt

# Grid dimensions
r_max = 4e6  # 4000 km
z_max = 1e6  # Vertical extent of vortex (1,000 km up/down)
points = 300  # Resolution

# Generate 3D cylindrical coordinates
r = np.linspace(0, r_max, points)
theta = np.linspace(0, 2 * np.pi, points)
z = np.linspace(-z_max, z_max, points)
R, THETA, Z = np.meshgrid(r, theta, z, indexing='ij')

# Vortex harmonic parameters
n_symmetry = 6  # hexagonal symmetry
k_r = 2 * np.pi / (r_max / 10)  # radial frequency
k_z = 2 * np.pi / (z_max / 8)   # vertical frequency
phase_shift = np.pi / 2         # phase delay for spiral effect

# Create 3D vortex wave function
vortex = np.sin(n_symmetry * THETA + k_r * R - k_z * Z + phase_shift)

# Normalize to -1 to 1
vortex /= np.max(np.abs(vortex))

# Plot: Midplane slice (theta vs z at fixed radius)
plt.figure(figsize=(8, 6))
slice_idx = points // 2  # slice at midpoint in radius
plt.imshow(vortex[slice_idx, :, :], cmap='plasma', aspect='auto',
           extent=[-z_max, z_max, 0, 2 * np.pi])
plt.colorbar(label='Wave Interference Intensity')
plt.title("Vertical Spiral Harmonic Slice (θ vs z) from Saturn Hexagonal Vortex Model")
plt.xlabel("z (vertical) [km]")
plt.ylabel("θ (angular radians)")
plt.tight_layout()
plt.savefig("saturn_3dvortex_harmonic_model.png", dpi=300)
