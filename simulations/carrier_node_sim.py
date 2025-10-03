# carrier_node_sim.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Parameters ---
num_modes = 3                       # number of standing wave modes
omega = np.array([1.0, 2.0, 3.0])   # natural frequencies
gamma = 0.05                        # damping
K = 0.2                             # coupling strength
F0 = 0.1                            # external forcing amplitude
Omega_ext = 2.0                      # external driver frequency

# --- ODE system ---
def carrier_dynamics(t, y):
    A = y[:num_modes]          # amplitudes
    dA = y[num_modes:]         # velocities

    d2A = []
    for n in range(num_modes):
        coupling = K * np.sum(A) - K * A[n]    # simple global coupling
        drive = F0 * np.sin(Omega_ext * t)
        d2A.append(-2*gamma*dA[n] - omega[n]**2 * A[n] + coupling + drive)

    return np.concatenate([dA, d2A])

# --- Initial conditions ---
y0 = np.random.rand(2*num_modes) * 0.1
t_span = (0, 200)
t_eval = np.linspace(*t_span, 5000)

# --- Solve ---
sol = solve_ivp(carrier_dynamics, t_span, y0, t_eval=t_eval, method="RK45")

# --- Plot results ---
fig, ax = plt.subplots(figsize=(10, 6))
for n in range(num_modes):
    ax.plot(sol.t, sol.y[n], label=f'Mode {n+1}')
ax.set_title("Carrier Node Simulation: Mode Amplitudes")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.legend()
plt.savefig("carrier_modes.png", dpi=300)
plt.close()

# --- Phase-space view for mode 1 ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(sol.y[0], sol.y[num_modes], lw=0.8)
ax.set_title("Phase Space (Mode 1)")
ax.set_xlabel("A1")
ax.set_ylabel("dA1/dt")
plt.savefig("carrier_phase.png", dpi=300)
plt.close()
