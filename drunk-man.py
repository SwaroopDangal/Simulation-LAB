import random
import matplotlib.pyplot as plt

Steps = 100

x = 0
y = 0

X_positions = [x]
Y_positions = [y]

for i in range(Steps):
    direction = random.choice(["Left", "Right", "Straight"])

    if direction == "Left":
        x = x - 1
    elif direction == "Right":
        x = x + 1
    else:
        y = y + 1

    X_positions.append(x)
    Y_positions.append(y)

plt.figure(figsize=(8, 6))

plt.plot(X_positions, Y_positions, marker='o', markersize=3)

plt.scatter(X_positions[0], Y_positions[0],
            color='green', label='Start')

plt.scatter(X_positions[-1], Y_positions[-1],
            color='red', label='End')

plt.title("Random Walk Simulation of a Drunk Person")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.legend()

plt.show()