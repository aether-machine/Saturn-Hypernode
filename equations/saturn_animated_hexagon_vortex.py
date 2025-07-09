import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
R_max = 4e6  # max radius in km
n = 6        # 6-fold symmetry for the hexagon
omega_base = 2 * np.pi / (10 * 86400)  # base angular frequency ~10 day period (in seconds^-1)
k = 2 * np.pi / 2e5  # spatial frequency (tune this for scale)

# Grid
res = 500
x = np.linspace(-R_max, R_max, res)
y = np.linspace(-R_max, R_max, res)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Animation settings
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Evolving Saturn Vortex Hexagon")
ax.set_xlabel("km")
ax.set_ylabel("km")
img = ax.imshow(np.zeros_like(R), extent=[-R_max, R_max, -R_max, R_max],
                cmap='plasma', origin='lower', vmin=-1, vmax=1)

# Time-evolving wave function
def update(frame):
    t = frame * 1e5  # time in seconds
    phase = omega_base * t
    Z = np.sin(k * R - phase) * np.cos(n * Theta - 0.5 * phase)
    img.set_data(Z)
    return [img]

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Save or display
ani.save("saturn_hexagon_vortex.mp4", fps=20, dpi=150)
plt.savefig("saturn_hexagon_vortex.png", dpi=300)
