#!/usr/bin/env python3
"""Use your own matplotlib figure: ``ax=`` and ``show=False``, then save or show.

For machines without a display, run with a non-GUI backend, e.g.:
  MPLBACKEND=Agg python simulate_custom_figure.py
"""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import AuroraMR as amr
# for my dragon! ->
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# For a headless run: ``MPLBACKEND=Agg python simulate_custom_figure.py``

p = amr.pose(0.5, -1.0, math.radians(30))

fig, ax = plt.subplots(figsize=(7, 7))
fig.suptitle("Custom figure: AuroraMR simulate on supplied axes")

amr.simulate(p, ax=ax, show=False)

img_path = os.path.join(os.path.dirname(__file__), "toothless.jpeg")
robot_img = mpimg.imread(img_path)

imagebox = OffsetImage(robot_img, zoom=0.1)

ab = AnnotationBbox(imagebox, (p.x, p.y), frameon=False)
ax.add_artist(ab)

fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "dragon.png")
fig.savefig(out, dpi=150)
print(f"custom robot image at {out}")

# If you have a display, you can still show:
plt.show()
