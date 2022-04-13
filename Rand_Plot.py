import matplotlib.pyplot as plt
import random as rand

data = [rand.randint(1, 100) for i in range(100)]
plt.plot(data)
plt.show()
