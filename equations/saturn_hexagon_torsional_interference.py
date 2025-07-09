import numpy as np
import matplotlib.pyplot as plt

# Spatial grid
size = 800  # resolution
lim = 4e6   # in kilometers
x = np.linspace(-lim, lim, size)
y = np.linspace(-lim, lim, size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)

# Moons: semi-major axis in km
moons = {
    'Mimas': 185520,
    'Enceladus': 238020,
    'Tethys': 294660,
    'Dione': 377400,
    'Rhea': 527040,
    'Titan': 1221870
}

# Wave interference parameters
wavelengths = list(moons.values())
amplitudes = [1.0 for _ in wavelengths]

# Spiral torsion parameters
tau = 3.2    # torsional coefficient (tweak for tighter or looser spiral arms)
epsilon = 1e3  # prevent log(0)

# Apply torsional modulation
theta_mod = theta + tau * np.log(R + epsilon)

# Interference pattern with 6-fold symmetry and spiral torsion
Z = np.zeros_like(R)
for A, λ in zip(amplitudes, wavelengths):
    radial_wave = np.sin(2 * np.pi * R / λ)
    angular_wave = np.cos(6 * theta_mod)  # 6-fold symmetry
    Z += A * radial_wave * angular_wave

# Normalize
Z /= len(wavelengths)

# Plotting
plt.figure(figsize=(10, 10))
plt.imshow(Z, extent=(-lim, lim, -lim, lim), origin='lower', cmap='plasma')
plt.title("Saturn Hexagon Vortex Model with Spiral Torsion")
plt.xlabel("km")
plt.ylabel("km")
plt.colorbar(label='Wave Interference Intensity')
plt.tight_layout()
plt.savefig("saturn_torsional_inteference.png", dpi=300)
