import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

orbit = pyasl.KeplerEllipse(a=1.0, per=1.0, e=0.5, Omega=0.0, i=10.0, w=0.0)

t = np.linspace(0, 4, 200)
pos = orbit.xyzPos(t)

plt.style.use('dark_background')
fig, ax = plt.subplots()
l = plt.plot(pos[::, 1], pos[::, 0], 'k-')

red_dot, = plt.plot(pos[0][1], pos[0][0], 'wo')

def animate(i):
    red_dot.set_data(pos[i][1], pos[i][0])
    return red_dot,


myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0, len(t), 1), interval=40,
                                      blit=True, repeat=True)

plt.plot(0, 0, 'bo', markersize=9, label="Earth")

plt.plot(pos[::, 1], pos[::, 0], 'k-', label="Satellite Trajectory")
plt.legend(loc="upper right")
plt.title('Orbital Simulation')
plt.tick_params(
    axis='both',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False,
    left=False,
    labelleft=False)
plt.axis('off')
plt.show()
