import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa

x, y = np.meshgrid(np.linspace(0, 2*np.pi, 20), np.linspace(0, 2*np.pi, 20))

u, v = np.sin(x)*np.cos(y), np.cos(x)*np.sin(y)

dt = 0.01

fig, ax = plt.subplots(2, 2, figsize=(10, 10))
streamline = ax[0, 0].quiver(x, y, u, v)
ax[0, 0].set_xlim(0, 2 * np.pi)
ax[0, 0].set_ylim(0, 2 * np.pi)
ax[0, 0].set_title("Streamlines")

euler = ax[0, 1].quiver(x, y, u, v)
ax[0, 1].set_xlim(0, 2 * np.pi)
ax[0, 1].set_ylim(0, 2 * np.pi)
ax[0, 1].set_title("Eulerian field")

ax[1, 1].set_title("Pathlines")
ax[1, 0].set_title("Streaklines")

plt.suptitle("A1.3")
def uvfunc(x1, y1, t):
    return dt * np.sin(x1 + t) * np.cos(y1), dt * np.cos(x1 + t) * np.sin(y1)

#number of pathlines
n = 10

X = []
Y = []
pathlines = []
for i in range(n):

    X.append([np.random.rand()*2*np.pi])
    Y.append([np.random.rand()*2*np.pi])
    pathline, = ax[1, 1].plot(X[i], Y[i])
    pathlines.append(pathline)


def animate(i):
    ax[0, 0].clear()
    ax[0, 1].clear()
    x, y = np.meshgrid(np.linspace(0, 2 * np.pi, 20), np.linspace(0, 2 * np.pi, 20))
    t = dt * i
    u, v = np.sin(x+t) * np.cos(y), np.cos(x+t) * np.sin(y)
    streamline = ax[0, 0].streamplot(x, y, u, v, color='g')
    ax[0, 0].set_xlim(0, 2 * np.pi)
    ax[0, 0].set_ylim(0, 2 * np.pi)
    ax[0, 0].set_title("Streamlines")

    euler = ax[0, 1].quiver(x, y, u, v)
    ax[0, 1].set_xlim(0, 2 * np.pi)
    ax[0, 1].set_ylim(0, 2 * np.pi)
    ax[0, 1].set_title("Eulerian field")

    for j in range(n):
        x = X[j][-1]
        y = Y[j][-1]
        dx, dy = uvfunc(x, y, t)
        x += dx
        y += dy

        X[j].append(x)
        Y[j].append(y)
        pathlines[j].set_data(X[j], Y[j])
    return streamline, pathlines, euler

anim = fa(fig, animate, frames = 200, interval= 3)
anim.save("A1.3.gif", fps=30, writer="Pillow")

# plt.show()