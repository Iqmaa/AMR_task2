#!/usr/bin/env python3
"""Four-wheel Ackermann: rear axle pose, front wheels steer; four dotted tire traces."""
# WHAT IS AN ACKERMANN(AOT?): basically the normal car we drive?
# has specific drive wheels and steering wheels separate(inner wheel turns more than outer wheel)
# so basically a caster wheel?

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

# all motions are literally just the same format

params = amr.AckermannParams(#self explanatory
    wheelbase=0.55,
    track_width=0.36,
    max_steering_angle=0.5,
    max_speed=1.0,
)
session = amr.MotionSession.create(#self explanatory at this point
    amr.pose(0.0, 0.0, 0.0), #origin pose
    amr.KinematicsModel.ACKERMANN,
    dt=0.02, #timestep to update motion
    ackermann=params,
)

#self explanatory
session.forward(2.0, 0.6)
session.turn_left(math.radians(35), 0.8)
session.forward(1.5, 0.5)

fig, ax = plt.subplots(figsize=(8, 8)) #canvas
amr.plot_motion(session, ax=ax, show=False) #plot motion
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_ackermann_demo.png"), dpi=150)
print("Saved motion_ackermann_demo.png")
