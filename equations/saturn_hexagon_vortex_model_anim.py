import numpy as np
import matplotlib.pyplot as plt

# Constants
AU = 1.496e8  # km
saturn_radius = 58232  # in km

# Saturn's major moons with orbital radius (km) and period (days)
moons = {
    'Mimas':     {'radius': 185539,  'period': 0.942},
    'Enceladus': {'radius': 238037,  'period': 1.370},
    'Tethys':    {'radius': 294672,  'period': 1.888},
    'Dione':     {'radius': 377415,  'period': 2.737},
    'Rhea':      {'radius': 527068,  'period': 4.518},
    'Titan':     {'radius': 1221870, 'period': 15.945}
}

# Influence weight based on 1 / radius (simplified assumption)
for m in moons:
    moons[m]['freq'] = 2 * np.pi / (moons[m]['period'])  # angular frequency in rad/day
    moons[m]['weight'] = 1 / moons[m]['radius']

# Grid setup
grid_size = 800
extent = 4e6
x = np.linspace(-extent, extent, grid_size)
y = np.linspace(-extent, extent, grid_size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Initialize vortex field
Z = np.zeros_like(R)

# Add 6-fold angular symmetry
N = 6  # Hexagonal
angular_component = np.cos(N * Theta)

# Simulate standing wave from moons
for moon in moons.values():
    radial_wave = np.sin(2 * np.pi * R / moon['radius'] - moon['freq'])  # phase shift simulates motion
    Z += moon['weight'] * radial_wave * angular_component

# Normalize
Z /= np.max(np.abs(Z))

# Plot
plt.figure(figsize=(8, 8))
plt.title("Enhanced Saturn Hexagon Vortex Model")
plt.imshow(Z, cmap='plasma', extent=[-extent, extent, -extent, extent])
plt.colorbar(label="Wave Interference Intensity")
plt.xlabel('km')
plt.ylabel('km')
plt.axis('equal')
plt.tight_layout()
plt.savefig("saturn_hexagon_vortex_model.png", dpi=300)
