import numpy as np
import matplotlib.pyplot as plt

# Moon data: period (days), radius (km)
moons = {
    'Mimas': {'period': 0.942, 'radius': 185520},
    'Enceladus': {'period': 1.370, 'radius': 238020},
    'Tethys': {'period': 1.888, 'radius': 294660},
    'Dione': {'period': 2.737, 'radius': 377400},
    'Rhea': {'period': 4.518, 'radius': 527040},
    'Titan': {'period': 15.945, 'radius': 1221870},
    'Hyperion': {'period': 21.28, 'radius': 1481100},
    'Iapetus': {'period': 79.33, 'radius': 3561300}
}

# Simulation grid
size = 1000
x = np.linspace(-4e6, 4e6, size)
y = np.linspace(-4e6, 4e6, size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Wavelength scaling constant (to exaggerate wave features)
scale_factor = 1e5

# Wave interference superposition
field = np.zeros_like(R)

for moon in moons.values():
    wavelength = moon['period'] * scale_factor
    phase = 2 * np.pi * R / wavelength
    field += np.cos(phase)

# Normalize
field /= len(moons)

# Visualization
plt.figure(figsize=(8, 8))
plt.imshow(field, extent=[-4e6, 4e6, -4e6, 4e6], cmap='plasma')
plt.title("Vortex Interference Model from Saturn's Moons")
plt.xlabel("km")
plt.ylabel("km")
plt.colorbar(label='Wave Interference Intensity')
plt.savefig("saturn_equation.png", dpi=300)

