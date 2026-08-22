import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N = 1000
low = 1
high = 10

random_numbers = np.random.randint(low, high + 1, N)

observed = np.bincount(
    random_numbers,
    minlength=high + 1
)[low:high + 1]

expected = np.full(high - low + 1, N / (high - low + 1))

chi2, p = stats.chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Observed frequencies:", observed)
print("Expected frequencies:", expected)
print("Chi-square statistic:", round(chi2, 4))
print("P-value:", round(p, 6))

if p < 0.05:
    print("Decision: Reject H0")
    print("Conclusion: The random numbers are not uniformly distributed.")
else:
    print("Decision: Accept H0")
    print("Conclusion: The random numbers are approximately uniformly distributed.")

numbers = np.arange(low, high + 1)
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(numbers - width/2, observed,
        width, label="Observed Frequency")

plt.bar(numbers + width/2, expected,
        width, label="Expected Frequency")

plt.xlabel("Random Number")
plt.ylabel("Frequency")
plt.title("Chi-Square Test for Random Number Distribution")
plt.xticks(numbers)
plt.legend()
plt.grid(True, axis='y')
plt.show()