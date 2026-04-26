# AMR_task2

<img width="600" alt="image" src="/dragon.png" />

## The struggles

So, the first thing I did was change the default green box as the bot model, because I needed something better, and that was surprisingly harder than I thought. like, I spent almost the whole day doing that.<br>

Turns out changing the path in the custom figure.py wasn't enough, I had to change it from the Aurora AMR library itself, and even finding the file the green polygon was defined was tough let alone changing it. But i did !! eventually.<br>

Kept getting a black box behind the dragon at some point, was because it was initially a jpeg and apparently those have no alpha channel so no inbuilt transparency and its harder to use for rotation. modified the library again to set transparency manually, cause even just converting the file to png didn't work since it wasn't originally like that

## Actual Assignment

I picked the following files to comment on. Basically all motions follow the same format<br>

- pose_basics.py (had to modify library again to rotate the image)
- simulate_custom-figure.py 
- live_kinematics_demo.py 
- motion_two_wheel.py
- motion_ackermann_demo.py (same as bicycle??)
- motion_bicycle_demo.py (same as ackermann??)
- motion_differential_demo.py 
- motion_mecanum_demo.py
- minimal_drive_and_play.py (changed speed here)
- mecanum holonomic

<br>I also defined some wheel types like Ackermann and Mecanum at the top of the code since I didn't teally know them before
