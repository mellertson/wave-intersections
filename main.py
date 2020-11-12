import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.animation
import numpy as np
import datetime

x = np.random.randint(0, 180, size=100)  # xcoordinate
y = np.random.randint(0, 100, size=100)  # ycoordinate
R = np.random.randint(3, 10, size=100)  # radius
b = np.random.rand(192, 100)  # parameter by which to judge if circle is drawn or not

# set up plot
fig, ax = plt.subplots()
ax.set_xlim([0, 180])
ax.set_ylim([0, 100])
ax.set_aspect("equal")
text = ax.text(0.5, 1.02, "", transform=ax.transAxes, ha="right")

# create 100 circles
circles = []
for i in range(100):
	c = matplotlib.patches.Circle((x[i], y[i]), radius=R[i], color="r", alpha=0.6, fill=False)
	circles.append(c)
	# add them already to the plot
	ax.add_artist(c)


def totime(t):
	minutes = datetime.timedelta(seconds=t * 10 * 60)
	d = datetime.datetime(1, 1, 1) + minutes
	return "{}h{:2d}".format(d.hour, d.minute)


def update(t):
	text.set_text(totime(t))
	for i in range(100):
		# depending on condition set circle visible or not
		if b[t, i] > 0.6:
			circles[i].set_visible(True)
		else:
			circles[i].set_visible(False)
	# redraw the canvas
	fig.canvas.draw()


# call for single plot
update(92)
# call for animation
ani = matplotlib.animation.FuncAnimation(fig, update, interval=300, frames=192)

plt.show()