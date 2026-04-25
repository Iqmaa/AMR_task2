#!/usr/bin/env python3 
# tells terminal to use python to run this file
"""Use your own matplotlib figure: ``ax=`` and ``show=False``, then save or show.

For machines without a display, run with a non-GUI backend, e.g.:
  MPLBACKEND=Agg python simulate_custom_figure.py
"""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg #to read image pixels from a file

import AuroraMR as amr
# allows us to place an image at a specific x,y coordinate on a graph
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# For a headless run: ``MPLBACKEND=Agg python simulate_custom_figure.py``

p = amr.pose(0.5, -1.0, math.radians(30)) #robot's pose

fig, ax = plt.subplots(figsize=(7, 7)) #creates space for the graph
fig.suptitle("Custom figure: AuroraMR simulate on supplied axes") #as the name says

amr.simulate(p, ax=ax, show=False) #actually draws the graph into the space

img_path = os.path.join(os.path.dirname(__file__), "toothless.jpeg") #finding the image file
robot_img = mpimg.imread(img_path) #reads the image

imagebox = OffsetImage(robot_img, zoom=0.1)#wraps image in container for control

ab = AnnotationBbox(imagebox, (p.x, p.y), frameon=False) #puts image on coordinates
ax.add_artist(ab) #puts the image on the graph

fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "dragon.png")  #defines where to stor final image
fig.savefig(out, dpi=150) #stores final image in high quality
print(f"custom robot image at {out}")

# If you have a display, you can still show:
plt.show() #opens the image window
