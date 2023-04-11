


# author: Ethan Liu
# date: 3/2/2023
# file: surfaces3D.py
# input: none
# output: Graphs of various 3D shapes

import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)           # make a mesh, two 2D arrays, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')
plt.show()


ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)

Z = (X** 2) + (Y** 2)

X, Y = np.meshgrid(x,y)
ax.contour3D(X, Y, Z, 50)
ax.set_title("Elliptic Paraboloid")
plt.show()


ax = plt.axes(projection='3d')
theta = np.linspace(0, np.pi, 30)
a=3
alpha = np.linspace(0, 2 * np.pi, 30)
x = 2 * np.outer(np.cos(theta), np.sin(alpha))
y = 3 * np.outer(np.sin(theta), np.sin(alpha))
z = 4 * np.outer(np.ones_like(theta), np.cos(alpha))
ax.set_title("Ellipsoid")
ax.contour3D(x, y, z, 40)
plt.show()

ax = plt.axes(projection='3d')
a, b = np.mgrid[0:2*np.pi:100j, 0:np.pi:80j]
x = np.cos(a) * np.sin(b)
y = np.sin(a) * np.sin(b)

z = np.sqrt(x ** 2 + y **2)
ax.contour3D(x, y, z, 40)
ax.set_title("Cone")
plt.show()

ax = plt.axes(projection='3d')
Z = np.zeros([30, 30])
x = Z.shape[0]
y = Z.shape[1]
a=1
for i in range(x // 2):
    for j in range(i, x - i):
        for h in range(i, x - i):
            Z[j, h] = i
X, Y = np.meshgrid(range(x), range(y))
ax.contour3D(X, Y, Z, 50)
ax.set_title("Square Pyramid")
plt.show()

ax = plt.axes(projection='3d')
theta = np.arange(1,10,2)*np.pi/4
phigrid, thetagrid = np.meshgrid(theta, theta)
a=2
x = np.cos(phigrid)*np.sin(thetagrid)
y = np.sin(phigrid)*np.sin(thetagrid)
z = np.cos(thetagrid)/np.sqrt(2)
ax.contour3D(x*3, y*2, z*3, 40)
ax.set_title("Parallelpiped")
plt.show()