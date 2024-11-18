import matplotlib.pyplot as plt
import math

# Create an empty list for the points for our axes
x = []
y = []
# Generates 200 points on a sine wave
for i in range(200):
    x.append(i)
    y.append(math.sin(2 * math.pi * i / 10))

# Sets up x and y plot, graph title and axis names.
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.show()
