import matplotlib.pyplot as plt
import math


HERTZ = range(1, 10)
SIDES = range(3, 4)
CANVAS_SIZE = [-10, 10]
WAVES = 200
COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',]


def get_vertices(sides):
	vertices = []
	for degrees in range(0, 360, int(360/sides)):
		radians = math.radians(degrees)
		x = math.cos(radians)
		y = math.sin(radians)
		vertices.append((x, y))
		print(f'({x}, {y}) for degrees: {degrees}, radians: {radians}')
	return vertices


def get_waves(vertex, hertz, color):
	circles = []
	delta = 1/hertz
	for i in range(WAVES):
		circles.append(plt.Circle(vertex, delta * i, color=color, fill=False))
	return circles


def create_plot(sides, hertz):
	fig, ax = plt.subplots()
	ax.add_artist(plt.Circle((0,0), 0.05, color='black', fill=True))
	vertices = get_vertices(sides)
	for vertex in vertices:
		color = COLORS[vertices.index(vertex)]
		waves = get_waves(vertex, hertz, color)
		for wave in waves:
			ax.add_artist(wave)

	fig.canvas.draw()
	plt.ylim(CANVAS_SIZE)
	plt.xlim(CANVAS_SIZE)
	fig.savefig(f'waves-{sides}-sides.{hertz}-hertz.png')
	plt.show()


for hertz in HERTZ:
	for sides in SIDES:
		create_plot(sides, hertz)