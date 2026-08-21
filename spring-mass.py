import numpy as np
import matplotlib.pyplot as plt

F = 7
w = 0.7
t0 = 0
T = 50
dt = 0.01

N = int((T-t0)/dt)
t = np.arange(0, N) * dt

def du(u, z):
    return np.array([u[1], (F-u[0]) - 2*z*w*u[1]])

u = np.zeros((N, 2))
u[0] = [0, 0]

plt.figure(figsize=(10, 6))

damping_ratios = [0.05, 0.2, 1, 3]
line_styles = ['-', '--', '-.', ':']

for z, ls in zip(damping_ratios, line_styles):
    u[:] = 0
    u[0] = [0, 0]

    for i in range(N-1):
        m1 = du(u[i], z)
        m2 = du(u[i] + dt*m1/2, z)
        m3 = du(u[i] + dt*m2/2, z)
        m4 = du(u[i] + dt*m3, z)

        u[i+1] = u[i] + dt*(m1 + 2*m2 + 2*m3 + m4)/6

    plt.plot(t, u[:, 0], label=f'z={z}', linestyle=ls)

plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t) (m)")
plt.title("Response of Spring-Mass-Damper System")
plt.grid(True)
plt.legend()
plt.show()