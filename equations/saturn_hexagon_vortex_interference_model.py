import numpy as np
import matplotlib.pyplot as plt

# Constants
km_per_pixel = 1e4  # resolution scaling
grid_range_km = 4e6  # 4 million km in each direction

# Define moons: (name, orbital radius in km)
moons = [
    ("Mimas", 185540),
    ("Enceladus", 238020),
    ("Tethys", 294660),
    ("Dione", 377400),
    ("Rhea", 527040),
    ("Titan", 1221870),
    ("Hyperion", 1481100),
    ("Iapetus", 3561300)
]

# Grid setup
n_points = 1000
x = np.linspace(-grid_range_km, grid_range_km, n_points)
y = np.linspace(-grid_range_km, grid_range_km, n_points)
X, Y = np.meshgrid(x, y)

# Polar coordinates
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Construct vortex interference field
field = np.zeros_like(R)
n_fold_symmetry = 6  # hexagonal harmonic

for name, radius in moons:
    # Radial wave component centered on orbital radius
    k = 2 * np.pi / radius
    wave = np.cos(k * R - n_fold_symmetry * Theta)

    # Logarithmic damping for distance
    damping = 1 / (1 + np.log(1 + (np.abs(R - radius) / 1e5)))

    # Combine components
    field += wave * damping

# Normalize
field /= np.max(np.abs(field))

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(field, extent=[-grid_range_km, grid_range_km, -grid_range_km, grid_range_km],
           origin='lower', cmap='plasma')
plt.colorbar(label='Wave Interference Intensity')
plt.title("Saturn Hexagon Vortex Model (Enhanced Interference Harmonic)")
plt.xlabel('km')
plt.ylabel('km')
plt.tight_layout()
plt.savefig("saturn_hexagon_vortex_interference_model.png", dpi=300)
