import math

import AuroraMR as amr

# self explanatory too but it was nice to watch
s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.05)
s.forward(1.0, 0.5)
s.turn_left(math.pi / 4, 1.0)
s.forward(0.5, 0.5)
s.turn_right(math.pi / 6, 1.0)
s.forward(0.5, 0.5)
s.turn_left(math.pi, 1.0)
s.forward(1.0, 0.5)

# changing playback speed did nothing?
# changed dt and it worked, why?
# remeber thats how frequently its calculating position so even if you change speed it won't show it cause its only updating at the specified time stamp
amr.play_motion(s, playback_speed=10.0, log=True, show=True)

