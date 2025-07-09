import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Saturn's major moons with approximate orbital radii (in km) and arbitrary frequency scalings
moons = {
    'Mimas': 185540,
    'Enceladus': 238020,
    'Tethys': 294660,
    'Dione': 377400,
    'Rhea': 527040,
    'Titan': 1221870
}

# Simulation grid
size = 8000000  # km
resolution = 1000
x = np.linspace(-size, size, resolution)
y = np.linspace(-size, size, resolution)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Parameters
omega = 2 * np.pi / 100  # Base angular frequency
hex_symmetry = 6  # 6-fold rotational symmetry

# Time evolution settings
frames = 200
interval = 50  # ms

# Superpose wave contributions from all moons
def generate_frame(t):
    time = t * 0.1
    wave = np.zeros_like(R)

    for moon, radius in moons.items():
        freq = omega * (radius / moons['Mimas'])  # Scale frequencies
        phase = freq * time
        radial_component = np.sin(2 * np.pi * (R / radius) - phase)
        damping = np.exp(-R / (2e6))  # Radial decay
        wave += radial_component * damping

    # Add hexagonal (6-fold) twist
    hex_component = np.sin(hex_symmetry * Theta + omega * time)
    combined_wave = wave * hex_component

    return combined_wave

# Set up animation
fig, ax = plt.subplots(figsize=(8, 8))
cmap = plt.get_cmap('plasma')
vmin, vmax = -1.0, 1.0
img = ax.imshow(generate_frame(0), extent=(-size, size, -size, size),
                cmap=cmap, vmin=vmin, vmax=vmax, origin='lower')

ax.set_title("Saturn Hexagon Vortex Model (Animated Harmonics)")
ax.set_xlabel("km")
ax.set_ylabel("km")

def animate(t):
    frame = generate_frame(t)
    img.set_data(frame)
    return [img]

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)

plt.tight_layout()
plt.savefig("saturn_hexagon_vortex_model.png", dpi=300)
