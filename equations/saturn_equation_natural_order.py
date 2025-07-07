import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import sympy as sp

# === Define Saturn's moons data ===
moons = {
    'Mimas': {'orbital_radius': 185539, 'period': 0.942, 'mass': 3.75e19},
    'Enceladus': {'orbital_radius': 238042, 'period': 1.37, 'mass': 1.08e20},
    'Tethys': {'orbital_radius': 294619, 'period': 1.89, 'mass': 6.17e20},
    'Dione': {'orbital_radius': 377396, 'period': 2.74, 'mass': 1.1e21},
    'Rhea': {'orbital_radius': 527108, 'period': 4.52, 'mass': 2.31e21},
    'Titan': {'orbital_radius': 1221870, 'period': 15.95, 'mass': 1.35e23},
}

# === Create spatial grid ===
L = 4e6  # 4 million km view around Saturn
N = 1000
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# === Parameters ===
base_wavelength = 2 * np.pi * 1e5  # adjustable scale factor
hex_symmetry = 6

# === Build interference pattern ===
interference = np.zeros_like(R)

for name, data in moons.items():
    freq = 1 / data['period']
    phase_offset = data['orbital_radius'] / 1e6  # rough offset scale
    mass_weight = data['mass'] / 1e23  # normalized weight

    # Radial and angular terms
    radial_wave = np.sin(2 * np.pi * R / (base_wavelength / freq) + phase_offset)
    angular_wave = np.cos(hex_symmetry * Theta + phase_offset)

    # Weighted contribution
    interference += mass_weight * radial_wave * angular_wave

# === Normalize output ===
interference /= np.max(np.abs(interference))

# === Plot the result ===
plt.figure(figsize=(8, 8))
plt.imshow(interference, cmap='plasma', extent=(-L, L, -L, L), origin='lower', norm=Normalize(-1,1))
plt.colorbar(label='Wave Interference Intensity')
plt.title("Refined Saturn Vortex Field (Mass/Phase Weighted)")
plt.xlabel("km")
plt.ylabel("km")
plt.tight_layout()
plt.savefig("saturn_equation_natural_order.png", dpi=300)
