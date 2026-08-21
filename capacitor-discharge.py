import numpy as np
import matplotlib.pyplot as plt

R = 1200
C = 0.0015
V0 = 15

t0 = 0
T = 8
dt = 0.01

t = np.arange(t0, T + dt, dt)
V = np.zeros(len(t))
V[0] = V0

for i in range(len(t)-1):
    dV = -V[i] / (R * C)
    V[i+1] = V[i] + dV * dt

plt.figure(figsize=(8,5))
plt.plot(t, V, color='blue', label='Capacitor Discharging')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Discharging Simulation')
plt.grid(True)
plt.legend()
plt.show()