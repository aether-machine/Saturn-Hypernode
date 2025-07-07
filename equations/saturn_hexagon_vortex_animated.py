import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the grid
grid_size = 1000
extent = 4e6  # 4 million km span
x = np.linspace(-extent, extent, grid_size)
y = np.linspace(-extent, extent, grid_size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Saturn's moon orbital radii (km) and arbitrary mass-based amplitudes
moons = {
    'Mimas': (185539, 0.8),
    'Enceladus': (238042, 0.9),
    'Tethys': (294672, 1.0),
    'Dione': (377396, 1.1),
    'Rhea': (527108, 1.3),
    'Titan': (1221870, 2.0)
}

# Angular harmonic (6-fold symmetry)
angular_mode = 6

# Time values (simulate over ~10 orbital periods of Titan)
frames = 200
time_vals = np.linspace(0, 2 * np.pi * 10, frames)

# Precompute waveforms
def compute_frame(t):
    total_wave = np.zeros_like(R)
    for name, (radius, amplitude) in moons.items():
        radial_freq = 2 * np.pi / radius
        phase = radial_freq * R - angular_mode * Theta - t * radial_freq
        wave = amplitude * np.cos(phase)
        total_wave += wave
    return total_wave / len(moons)

# Animation function
def update(frame):
    wave = compute_frame(time_vals[frame])
    img.set_array(wave)
    return [img]

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Saturn Hexagon Vortex Model – Time Evolution")
img = ax.imshow(compute_frame(0), cmap='plasma', origin='lower',
                extent=[-extent, extent, -extent, extent],
                vmin=-1, vmax=1)
ax.set_xlabel('km')
ax.set_ylabel('km')
plt.colorbar(img, label="Wave Interference Intensity")

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=50)

# Save or display
ani.save("saturn_vortex_animation.mp4", fps=20)  # Optional save
plt.savefig("saturn_hexagon_vortex.png", dpi=300)
