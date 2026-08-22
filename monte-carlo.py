import numpy as np
import matplotlib.pyplot as plt

N = 500000

X = np.random.rand(N)
Y = np.random.rand(N)

inside = X**2 + Y**2 <= 1

pi = 4 * np.sum(inside) / N

print("Estimated value of pi:", pi)
print("Actual value of pi:", np.pi)

plt.figure(figsize=(8,8))

plt.scatter(X[inside], Y[inside],
            color='r', s=3, label='Inside Quarter Circle')

plt.scatter(X[~inside], Y[~inside],
            color='b', s=2, label='Outside Quarter Circle')

plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Monte Carlo Estimation of Pi (Estimated π = {pi:.5f})")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()