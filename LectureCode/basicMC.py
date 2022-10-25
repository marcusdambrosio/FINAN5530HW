import numpy as np
import matplotlib.pyplot as plt

slots = 35
tries = 100000

outcomes = np.random.randint(0, slots, tries)
expected = np.full(slots + 1, tries/slots)
# print(outcomes)
# print(expected)

count, bins, patches = plt.hist(outcomes, slots)
plt.plot(bins, expected)
# plt.hist(outcomes, bins = 20)
plt.show()