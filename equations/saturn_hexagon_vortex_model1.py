import numpy as np
import matplotlib.pyplot as plt

# Constants
km = 1e3  # kilometers to meters (for clarity)
grid_size_km = 4e6  # spatial extent from center in km
resolution = 1000  # grid resolution

# Moon data (approx values)
moons = [
    {"name": "Mimas",     "r": 185_500, "w": 0.2},
    {"name": "Enceladus", "r": 238_000, "w": 0.5},
    {"name": "Tethys",    "r": 295_000, "w": 0.7},
    {"name": "Dione",     "r": 377_000, "w": 0.8},
    {"name": "Rhea",      "r": 527_000, "w": 1.0},
    {"name": "Titan",     "r": 1_222_000, "w": 3.0},
]

# Create 2D coordinate grid
x = np.linspace(-grid_size_km, grid_size_km, resolution)
y = np.linspace(-grid_size_km, grid_size_km, resolution)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)  # radial distance
Theta = np.arctan2(Y, X)  # angular position

# Initialize wave field
wave = np.zeros_like(R)

# Superimpose radial waves from each moon
for moon in moons:
    r0 = moon["r"]
    w = moon["w"]
    
    # Radial standing wave with damping (Gaussian envelope)
    k = 2 * np.pi / r0
    envelope = np.exp(-((R - r0) / (r0 * 0.15))**2)
    radial_wave = w * np.sin(k * R) * envelope

    wave += radial_wave

# Add angular (hexagonal) modulation
m = 6  # hexagonal symmetry
angular_mod = np.cos(m * Theta)
wave *= angular_mod

# Normalize for visualization
wave /= np.max(np.abs(wave))

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(wave, cmap='plasma', extent=(-grid_size_km, grid_size_km, -grid_size_km, grid_size_km))
plt.colorbar(label="Wave Interference Intensity")
plt.title("Saturn Hexagon Vortex Model (Wave Harmonics + Hexagonal Symmetry)")
plt.xlabel("km")
plt.ylabel("km")
plt.tight_layout()
plt.savefig("saturn_hexagon_vortex_model1.png", dpi=300)
