import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa

x, y = np.meshgrid(np.linspace(0, 2*np.pi, 50), np.linspace(0, 2*np.pi, 50))

u = np.sin(x)*np.cos(y)
v = np.cos(x)*np.sin(y)

# streamlines, eulerian field and interpolated paths
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
ax[0, 0].streamplot(x, y, u, v, colo    r='g')
ax[0, 0].set_xlim(0, 2 * np.pi)
ax[0, 0].set_ylim(0, 2 * np.pi)
ax[0, 0].set_title("Streamlines")

ax[0, 1].quiver(x, y, u, v)
ax[0, 1].set_xlim(0, 2 * np.pi)
ax[0, 1].set_ylim(0, 2 * np.pi)
ax[0, 1].set_title("Eulerian field")

plt.suptitle("A1.2")

# plotting the pathlines
dt = 0.01

ax[1, 1].set_title("Pathlines")
ax[1, 0].set_title("Streaklines")

def uvfunc(x, y):
    return dt * np.sin(x) * np.cos(y), dt * np.cos(x) * np.sin(y)

#number of pathlines
n = 10

X = []
Y = []
pathlines = []
streaklines = []
for i in range(n):

    X.append([np.random.rand()*2*np.pi])
    Y.append([np.random.rand()*2*np.pi])
    print(X[i][-1], Y[i][-1])
    pathline, = ax[1, 1].plot(X[i], Y[i])
    pathlines.append(pathline)
    streakline, =ax[1, 0].plot(X[i], Y[i])
    streaklines.append(streakline)


def animate(i):
    t = dt * i

    for j in range(n):
        x = X[j][-1]
        y = Y[j][-1]
        dx, dy = uvfunc(x, y)
        x += dx
        y += dy

        X[j].append(x)
        Y[j].append(y)
        pathlines[j].set_data(X[j], Y[j])
        streaklines[j].set_data(X[j], Y[j])
    return pathlines, streaklines


anim = fa(fig, animate, frames = 200, interval= 3)
anim.save("A1.2.gif", fps=30, writer="Pillow")