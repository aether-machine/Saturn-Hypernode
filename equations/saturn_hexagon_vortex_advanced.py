import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the spatial grid
grid_size = 1000
extent = 4e6  # 4 million km
x = np.linspace(-extent, extent, grid_size)
y = np.linspace(-extent, extent, grid_size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Saturn’s moon data (orbital radius in km, period in days, amplitude weight)
moons = {
    'Mimas':     (185539, 0.942, 0.8),
    'Enceladus': (238042, 1.37, 0.9),
    'Tethys':    (294672, 1.89, 1.0),
    'Dione':     (377396, 2.74, 1.1),
    'Rhea':      (527108, 4.52, 1.3),
    'Titan':     (1221870, 15.95, 2.0),
}

# Angular harmonic symmetry
angular_mode = 6  # Hexagonal symmetry

# Time axis: simulate ~20 Titan periods
frames = 240
time_vals = np.linspace(0, 2 * np.pi * 20, frames)

# Envelope falloff function (energy dissipation from center)
def envelope(R, scale=3e6):
    return np.exp(-R**2 / (2 * scale**2))

# Compute one frame of the interference pattern
def compute_frame(t):
    total_wave = np.zeros_like(R)
    for name, (radius, period, amplitude) in moons.items():
        omega = 2 * np.pi / (period * 86400)  # Convert to rad/sec
        k = 2 * np.pi / radius  # Spatial frequency
        phase = k * R - angular_mode * Theta - omega * t * 1e5  # Scaled time
        local_wave = amplitude * np.cos(phase)
        total_wave += local_wave
    total_wave *= envelope(R)
    return total_wave / len(moons)

# Plot & animate
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Saturn Hexagon Vortex Model – Time Evolution")
img = ax.imshow(compute_frame(0), cmap='plasma', origin='lower',
                extent=[-extent, extent, -extent, extent],
                vmin=-1, vmax=1)
ax.set_xlabel('km')
ax.set_ylabel('km')
plt.colorbar(img, label="Wave Interference Intensity")

def update(frame):
    wave = compute_frame(time_vals[frame])
    img.set_array(wave)
    return [img]

ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=50)

# Save and display
ani.save("saturn_vortex_advanced.mp4", fps=20)
plt.savefig("saturn_vortex_final.png", dpi=300)

