import matplotlib.pyplot as plt
import math

x = []
y = []
for i in range(100):
    x.append(i)
    y.append(math.sin(2 * math.pi * i / 10))

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.show()
