import matplotlib.pyplot as plt

circles = []
circles.append(plt.Circle((0.5, 0.5), 0.2, color='blue', fill=False))
circles.append(plt.Circle((0.5, 0.5), 0.1, color='r', fill=False))

circles.append(plt.Circle((1, 1), 0.2, color='g'))

fig, ax = plt.subplots()

for circle in circles:
	ax.add_artist(circle)

fig.savefig('plotcircles.png')
fig.canvas.draw()
plt.show()