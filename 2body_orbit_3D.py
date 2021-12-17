import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

orbit = pyasl.KeplerEllipse(a=26600, per=0.5, e=0.737, Omega=0.0, i=63.4, w=270.0)

# Get a time axis
t = np.linspace(0, 4, 1000)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = orbit.xyzPos(t)

fig = plt.figure()
ax = p3.Axes3D(fig)

red_dot, = ax.plot(pos[::, 1], pos[::, 0], pos[::, 2], 'ro',
                   label="Satellite")


def animate(i, pos, red_dot):
    red_dot.set_data([pos[i][1], pos[i][0]])
    red_dot.set_3d_properties(pos[i][2])
    return red_dot,


# Create animation using the animate() function
ani = animation.FuncAnimation(fig, animate, len(t),
                              fargs=(pos, red_dot),
                              interval=100, blit=False)

ax.plot([0], [0], [0], 'bo', markersize=9, label='Earth')
ax.plot(pos[::, 1], pos[::, 0], pos[::, 2], 'k-',
        label="Satellite Trajectory")

# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.style.use('default')
plt.legend()
plt.title('Orbital Simulation')
plt.show()
