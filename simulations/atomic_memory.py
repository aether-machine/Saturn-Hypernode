import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Parameters ---
num_layers = 6        # number of shells/rings
points = 1000         # resolution per ring
amplitudes = np.linspace(1, 0.3, num_layers)  # decreasing amplitudes
frequencies = np.arange(1, num_layers + 1)    # harmonic frequencies

# --- Static Plot: Harmonic Shells ---
def generate_static(path="figures/atomic_shells.png"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    theta = np.linspace(0, 2 * np.pi, points)

    for n, (A, f) in enumerate(zip(amplitudes, frequencies), 1):
        r = n + A * np.sin(f * theta)  # base radius + harmonic perturbation
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y, label=f'Shell {n}')

    plt.title("Atomic Memory: Harmonic Shells", fontsize=14)
    plt.savefig(path, dpi=300)
    plt.close()

# --- Animation: Dynamic Harmonic Rings ---
def generate_animation(path="figures/atomic_memory.gif"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    lines = []
    for _ in range(num_layers):
        line, = ax.plot([], [], lw=1.5)
        lines.append(line)

    ax.set_xlim(-num_layers - 2, num_layers + 2)
    ax.set_ylim(-num_layers - 2, num_layers + 2)

    theta = np.linspace(0, 2 * np.pi, points)

    def update(frame):
        for i, (A, f, line) in enumerate(zip(amplitudes, frequencies, lines), 1):
            r = i + A * np.sin(f * theta + frame * 0.1)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            line.set_data(x, y)
        return lines

    ani = animation.FuncAnimation(fig, update, frames=200, blit=True, interval=50)
    ani.save(path, writer="pillow")
    plt.close()

# --- Main Execution ---
if __name__ == "__main__":
    import os
    os.makedirs("figures", exist_ok=True)
    generate_static()
    generate_animation()
