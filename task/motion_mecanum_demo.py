#!/usr/bin/env python3
"""Mecanum X-config: omnidirectional motion and four wheel traces (FL, FR, RL, RR)."""
# WHAT IS A MECANUM: A Mecanum system uses four specialized wheels that allow a robot to move in any direction; forward, backward, sideways (strafing), and diagonally without changing the direction its "nose" is pointing.
# strafing just means to move without changing orientation(rotation)

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

# all motions are literally just the same format

os.environ.setdefault("MPLBACKEND", "Agg") #headless mode, no popup
#          distance from  CentreToFront/back wheels      , CentreToLeft/right wheels
params = amr.MecanumParams(half_length_y=0.28, half_width_x=0.22, max_wheel_speed=2.5) #last is as described
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0), #origin pose
    amr.KinematicsModel.MECANUM,
    dt=0.015, #time between each calculation(frame change?) in millisec
    mecanum=params,
)

session.forward(1.0, 0.7) #move forward
session.strafe_right(0.8, 0.6) #move to right without turning
session.turn_left(math.pi / 3, 1.0) #turns(rotate)
session.mecanum_drive_wheels(0.5, -0.2, 0.0, 0.8, duration=1.0) #individual wheel movement

goal = amr.pose(1.5, 0.5, math.pi / 6) #target coordinates
session.drive_to_pose(goal, linear_speed=0.6, angular_speed=1.0, position_tol=0.1, angle_tol=0.12) #how to get there

fig, ax = plt.subplots(figsize=(8, 8))
amr.plot_motion(session, ax=ax, show=False) #draw each place the bot passes
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_mecanum_demo.png"), dpi=150) #saves drawing
print("Saved motion_mecanum_demo.png")
