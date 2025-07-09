import numpy as np
import matplotlib.pyplot as plt

# Define grid size
grid_size = 1000
space_extent = 4e6  # in km

x = np.linspace(-space_extent, space_extent, grid_size)
y = np.linspace(-space_extent, space_extent, grid_size)
X, Y = np.meshgrid(x, y)

# Convert to polar coordinates
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Saturn's main moons (approx orbital radius in km and relative phase offsets in radians)
moons = {
    "Mimas":      (185520, 0.0),
    "Enceladus":  (238020, 1.5),
    "Tethys":     (294660, 3.0),
    "Dione":      (377400, 2.2),
    "Rhea":       (527040, 4.7),
    "Titan":     (1221870, 0.9)
}

# Main vortex harmonic
n_fold = 6  # 6 for hexagon

# Initialize wave field
wave_field = np.zeros_like(R)

# Wave contribution from each moon
for moon, (r0, phase) in moons.items():
    # Create radial harmonic wave damped by 1/r
    radial_component = np.cos(2 * np.pi * (R - r0) / 1e5 - phase) * np.exp(-((R - r0)**2) / (2 * (1.5e5)**2))
    
    # Angular hexagonal contribution
    angular_component = np.cos(n_fold * Theta)

    # Combine contributions
    wave_field += radial_component * angular_component

# Normalize
wave_field /= np.max(np.abs(wave_field))

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(wave_field, extent=[-space_extent, space_extent, -space_extent, space_extent],
           cmap='plasma', origin='lower')
plt.title("Saturn Hexagon Vortex Model (Phase-Shifted & Damped Harmonics)")
plt.xlabel("km")
plt.ylabel("km")
cbar = plt.colorbar(label='Wave Interference Intensity')
plt.tight_layout()
plt.savefig("saturn_hexagon_3d.png", dpi=300)
