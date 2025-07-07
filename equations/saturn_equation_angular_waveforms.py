import numpy as np
import matplotlib.pyplot as plt

# Define grid
grid_size = 1000
x = np.linspace(-4e6, 4e6, grid_size)
y = np.linspace(-4e6, 4e6, grid_size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)

# Moons: [name, semi-major axis (km), weight (arbitrary)]
moons = [
    ("Mimas", 185539, 0.6),
    ("Enceladus", 237948, 0.8),
    ("Tethys", 294619, 0.7),
    ("Dione", 377396, 0.9),
    ("Rhea", 527108, 1.0),
    ("Titan", 1221870, 1.2)
]

# Parameters
wavelength_scale = 0.85e6
time = 0  # can evolve later

# Total wave field
wave_field = np.zeros_like(R)

for name, radius, weight in moons:
    # radial wave component
    k = 2 * np.pi / wavelength_scale
    phase = (radius / 1e6) + time * 1e-5  # orbital modulation
    radial_component = np.sin(k * R - phase)

    # angular 6-fold symmetry component (hexagonal harmonics)
    angular_modulation = np.cos(6 * theta + phase)

    # combine
    moon_wave = weight * radial_component * angular_modulation
    wave_field += moon_wave

# Normalize
wave_field /= np.max(np.abs(wave_field))

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(wave_field, cmap="plasma", extent=[-4e6, 4e6, -4e6, 4e6])
plt.title("Saturn Hexagon Vortex Model (With 6-Fold Symmetry Harmonic)")
plt.xlabel("km")
plt.ylabel("km")
plt.colorbar(label="Wave Interference Intensity")
plt.tight_layout()
plt.savefig("saturn_equation_updated.png", dpi=300)
