#!/usr/bin/env python3
"""Two-wheel (v, ω) model: forward, turn, backward, drive_to_pose with dotted tire traces."""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg") #headless mode

# all motions are literally just the same format

p0 = amr.pose(0.0, 0.0, 0.0) #origin pose
params = amr.TwoWheelParams(track_width=0.45, max_linear_speed=1.2, max_angular_speed=1.5) #as described
session = amr.MotionSession.create(p0, amr.KinematicsModel.TWO_WHEEL, dt=0.015, unicycle=params)

session.forward(1.5, 0.6) #move forward, the rest is as described wo
session.turn_left(math.pi / 2, 1.0)
session.forward(1.0, 0.6)
session.backward(0.5, 0.4)
goal = amr.pose(0.5, 2.0, math.pi / 6) #target pose
session.drive_to_pose(goal, linear_speed=0.7, angular_speed=1.2, position_tol=0.08, angle_tol=0.08) #how to get there

fig, ax = plt.subplots(figsize=(8, 8)) #creates canvas
amr.plot_motion(session, ax=ax, show=False) #draws movement history of bot
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_two_wheel_demo.png"), dpi=150) #save to file
print("Saved motion_two_wheel_demo.png, final pose:", session.pose)
