#!/usr/bin/env python3
"""Create poses and read ``x``, ``y``, ``theta``.

Heading convention: ``theta`` is in radians; ``0`` faces north (+y); increasing
counterclockwise (west = π/2, east = 3π/2 or −π/2).

Using ``import AuroraMR as amr`` does not load matplotlib until you call
``amr.simulate``. You can also use ``import amr`` or ``from amr.pose import Pose, pose``.
"""

from __future__ import annotations

import math

import AuroraMR as amr
import matplotlib.pyplot as plt

# Preferred: factory function
p = amr.pose(1.5, -0.5, math.pi / 6) #robot's positiom
print("pose() ->", p) #basically just prints out p ?
print("  x =", p.x, "  y =", p.y, "  theta (rad) =", p.theta) #print each positiona as specified by the text in the parenthesis

# Instantiate ``Pose`` directly if you already have values
q = amr.Pose(x=0.0, y=0.0, theta=0.0)
print("Pose(...) ->", q)

# just defining the poses for each cardinal points so the robot faces their respective directions
north = amr.pose(0, 1, 0)
west = amr.pose(0, -1, math.pi / 2) #90 deg
south = amr.pose(-1, 0, math.pi) #180 deg
east = amr.pose(1, 0, 3 * math.pi / 2) # 270 deg
print("north theta=0:", north.theta, " west theta=π/2:", west.theta) #shows the value of the angles(in degrees) in rad in the terminal

fig,ax = plt.subplots(figsize=(8,8))

# to see the robot in hte different directions, why is the image not rotating??
#tried just typing a plt.show() but that obviously didn't work
amr.simulate(north, ax=ax, show =False)
amr.simulate(south, ax=ax, show =False)
amr.simulate(east, ax=ax, show =False)
amr.simulate(west, ax=ax, show =False)

ax.set_xlim(-2, 2) #increasing the plot
ax.set_ylim(-2, 2)
plt.show()