import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Spatial grid
L = 4e6  # km range
res = 600  # resolution
x = np.linspace(-L, L, res)
y = np.linspace(-L, L, res)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Moon data: orbital radii (km) and periods (days converted to seconds)
moons = {
    'Mimas': (185539, 0.942 * 86400),
    'Enceladus': (238042, 1.37 * 86400),
    'Tethys': (294672, 1.89 * 86400),
    'Dione': (377415, 2.74 * 86400),
    'Rhea': (527108, 4.52 * 86400),
    'Titan': (1221870, 15.95 * 86400)
}

# Convert to frequency (Hz)
frequencies = {moon: 1 / period for moon, (_, period) in moons.items()}

# Wave function generator with 6-fold azimuthal symmetry
def generate_wave(t):
    wave = np.zeros_like(R)
    for moon, (radius, period) in moons.items():
        f = 1 / period
        omega = 2 * np.pi * f
        k = 2 * np.pi / radius
        phase = omega * t
        wave += np.cos(k * R - phase + 6 * Theta)
    return wave

# Animation setup
fig, ax = plt.subplots(figsize=(6, 6))
cmap = plt.cm.plasma
im = ax.imshow(generate_wave(0), cmap=cmap, extent=(-L, L, -L, L), animated=True)
ax.set_title("Time-Evolving Saturn Vortex Field")
ax.set_xlabel("km")
ax.set_ylabel("km")

def update(frame):
    t = frame * 0.5 * 86400  # time step (in seconds)
    wave = generate_wave(t)
    im.set_array(wave)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=120, interval=100, blit=True)

# Save animation (optional)
ani.save("saturn_vortex_evolution.mp4", fps=15, dpi=150)

plt.savefig("saturn_evolving_vortex_model.png", dpi=300)
