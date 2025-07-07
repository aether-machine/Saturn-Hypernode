import numpy as np
import matplotlib.pyplot as plt

# Define moon data: (name, semi-major axis [km], orbital period [days])
moons = [
    ("Mimas",      185520, 0.942),
    ("Enceladus",  238020, 1.370),
    ("Tethys",     294660, 1.888),
    ("Dione",      377400, 2.737),
    ("Rhea",       527040, 4.518),
    ("Titan",     1221870, 15.945),
]

# Spatial grid setup
L = 4e6  # size in km
res = 1000
x = np.linspace(-L, L, res)
y = np.linspace(-L, L, res)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Harmonic superposition with angular symmetry
wavefield = np.zeros_like(R)

n_symmetry = 6  # hexagonal symmetry
time = 0  # Can animate over time later

for name, radius, period in moons:
    k = 2 * np.pi / radius  # radial wavenumber
    omega = 2 * np.pi / period  # angular frequency
    
    # Gaussian radial envelope centered at moon's orbit
    envelope = np.exp(-((R - radius)**2) / (2 * (radius * 0.05)**2))
    
    # Rotating standing wave with angular symmetry
    phase = k * R - omega * time + n_symmetry * Theta
    wave = np.cos(phase) * envelope
    wavefield += wave

# Normalize
wavefield /= np.max(np.abs(wavefield))

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(wavefield, extent=[-L, L, -L, L], cmap='plasma')
plt.colorbar(label='Wave Interference Intensity')
plt.title("Saturn Vortex Harmonic from Orbital Resonance\n(Hexagonal Symmetry Overlay)")
plt.xlabel("km")
plt.ylabel("km")
plt.axis('equal')
plt.tight_layout()
plt.savefig("saturn_equation_orbital_vortex_resonance.png", dpi=300)
