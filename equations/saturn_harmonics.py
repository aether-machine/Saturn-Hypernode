import numpy as np
import matplotlib.pyplot as plt

# Orbital periods in Earth days (from Saturn moons)
moons = {
    "Mimas": 0.942,
    "Enceladus": 1.370,
    "Tethys": 1.888,
    "Dione": 2.737,
    "Rhea": 4.518,
    "Titan": 15.945
}

# Convert periods to angular frequencies (omega = 2π / T)
frequencies = {moon: 2 * np.pi / period for moon, period in moons.items()}

# Simulation time (1000 days sampled every 0.1 days)
t = np.linspace(0, 1000, 10000)

# Generate summed waveforms from all moons
total_wave = np.zeros_like(t)
individual_waves = {}

for moon, omega in frequencies.items():
    wave = np.sin(omega * t)
    individual_waves[moon] = wave
    total_wave += wave

# Plot the result
plt.figure(figsize=(12, 6))
plt.plot(t, total_wave, label='Total Interference Wave', color='black', linewidth=2)

# Optionally, show individual moon waves
for moon, wave in individual_waves.items():
    plt.plot(t, wave, alpha=0.3, label=moon)

plt.title("Interference Pattern from Saturn's Moons (Harmonic Simulation)")
plt.xlabel("Time (days)")
plt.ylabel("Amplitude (arbitrary units)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("saturn_harmonics.png", dpi=300)

