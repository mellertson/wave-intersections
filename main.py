#!/usr/bin/env python3
import matplotlib.pyplot as plt
import math


HERTZ = range(5, 21)
SIDES = range(3, 10)
CANVAS_SIZE = [-10, 10]
WAVES = 350
COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow',]
ALPHA = 0.75


class Colors(object):
	""" Iterates over matplotlib colors """
	def __init__(self):
		self.i = 0
	def __iter__(self):
		return self
	def __next__(self):
		self.i += 1
		if self.i >= len(COLORS):
			self.i = 0
		return COLORS[self.i]


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
	circles.append(plt.Circle(vertex, 0.075, color='black', fill=True))
	for i in range(WAVES):
		circles.append(
			plt.Circle(
				vertex,
				delta * i,
				color=color,
				fill=False,
				alpha=ALPHA,
			)
		)
	return circles


def create_plot(sides, hertz):
	fig, ax = plt.subplots()
	ax.add_artist(plt.Circle((0,0), 0.05, color='black', fill=True))
	vertices = get_vertices(sides)
	colors = Colors()
	for vertex in vertices:
		color = colors.__next__()
		waves = get_waves(vertex, hertz, color)
		for wave in waves:
			ax.add_artist(wave)

	fig.canvas.draw()
	plt.ylim(CANVAS_SIZE)
	plt.xlim(CANVAS_SIZE)
	plt.title(f'{sides} Equidistant Waves at {hertz}Hz')
	fig.savefig(f'waves-{WAVES}_sides-{sides}_hertz-{hertz}.png')
	plt.show()


for sides in SIDES:
	for hertz in HERTZ:
		create_plot(sides, hertz)