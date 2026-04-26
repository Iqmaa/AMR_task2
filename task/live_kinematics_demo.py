#!/usr/bin/env python3
"""Real-time matplotlib animation with optional teaching logs in the terminal.

Examples::

    # All four models, normal speed, formatted logs for students
    python live_kinematics_demo.py all --log

    # 2× faster playback, detailed multi-line logs every 20 frames
    python live_kinematics_demo.py mecanum --speed 2 --log --log-every 20 --log-detailed

    # Save video (no window); logs still go to terminal unless --quiet-log
    python live_kinematics_demo.py all --save out.mp4 --log
"""

from __future__ import annotations

import argparse #need this to pare arguments
import sys #to interact with terminal

import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt

import AuroraMR as amr

#each argument allows you change a specififc thing
def main() -> None:
    parser = argparse.ArgumentParser(description="Live AuroraMR kinematics demos with optional teaching logs")
    parser.add_argument( #this is to choose which model to run
        "mode",
        nargs="?", #can choose to not use any argument and it defaults to all
        default="all",
        choices=("all", "two_wheel", "unicycle", "differential", "ackermann", "mecanum"), 
        #the things you can pick between
        help="Model to play, or 'all' for all four in sequence (default: all)", #explanation to user
    )
    parser.add_argument(#time interval for simulation to update
        "--interval", type=int, default=28, help="Base milliseconds between frames (before speed)")
    parser.add_argument( #(does interval/speed) so you can increase interval, why not just increase directly?
        "--speed",
        type=float,
        default=1.0,
        help="Playback speed multiplier (>1 = faster, <1 = slower). Effective interval = interval/speed.",
    )
    parser.add_argument(#tells python to stop running after one iteration
        "--no-repeat", action="store_true", help="Do not loop the animation")
    parser.add_argument(#as described
        "--save", metavar="FILE", help="Save animation to file instead of showing")
    parser.add_argument(#printing every thing that happens (as described basically)
        "--log", action="store_true", help="Print teaching notes to the terminal while playing")
    parser.add_argument(#coordinates and how often to print them
        "--log-every",
        type=int,
        default=12,
        metavar="N",
        help="Log every N simulation frames (frame 0 always logged if --log)",
    )
    parser.add_argument(#as decribed
        "--log-detailed",
        action="store_true",
        help="Multi-line log blocks instead of one line per log step",
    )
    parser.add_argument(#as described
        "--log-file",
        metavar="PATH",
        help="Append logs to this file as well as stdout (still prints to terminal unless --quiet-log)",
    )
    parser.add_argument(#as described
        "--quiet-log",
        action="store_true",
        help="With --log-file, only write logs to the file (not stdout)",
    )

    # added this myself s it can run for longer, didn't work. Had to go do *2 i the library again
#    parser.add_argument(
# "--duration", type=float, default=5.0, help="Total seconds to run simulation")
    args = parser.parse_args()

    #there's others like TkAgg, Qt5Agg(both interactive). Agg: Anti-Grain Geometry
    #rAgg renders pixels directly to the computer's memory instead of trying to talk to your system
    if args.save: #tells matplotlib to use Agg because an interactive one could crash your system(too much)
        matplotlib.use("Agg")

    show_window = not args.save #just tells the comuter that if the users choose this they're doing the opposite of what was previously specified
    repeat = not args.no_repeat

    log_file = None
    log_stream = None
    if args.log_file:#'a' for append adds data to the end of the log file each time. w would have overwritten it
        log_stream = open(args.log_file, "a", encoding="utf-8")

    class _Tee: #allows you to pass data to more than one place(normally you can only send to one -screen or file)
        def __init__(self, *streams: object) -> None: #allowing 2 destinations
            self.streams = streams

        def write(self, data: str) -> None: #defining the destinations
            for s in self.streams:
                s.write(data) #sends data
                s.flush() #saves data

        def flush(self) -> None: #to prepare the location the data will be saved ?
            for s in self.streams:
                s.flush()

    if args.log: #runs if user wants logs
        if args.quiet_log and log_stream is not None:
            tee: object = log_stream #only sends to file doesn't print
        elif log_stream is not None:
            tee = _Tee(sys.stdout, log_stream) #does both
        else:
            tee = sys.stdout #no file specified print to screen
        log_opts = amr.PlaybackLogOptions(
            enabled=True,
            every_n_frames=max(1, args.log_every),
            detailed_block=args.log_detailed,
            file=tee,  # type: ignore[arg-type]
        )
    else:
        log_opts = None

    try: #if it doesn't it just ends loop(goes tofinally). Thats what try is for.
        if args.mode == "all": #as described before
            anim = amr.play_all_kinematics_live(
                interval_ms=args.interval,
                playback_speed=args.speed,
                repeat=repeat,
                show=show_window,
                log_options=log_opts,
            )
        else: #if you picked onlyone model, runs it
            anim = amr.play_motion_by_kind(
                args.mode,
                interval_ms=args.interval,
                playback_speed=args.speed,
                show=show_window,
                log_options=log_opts,
                # duration=args.duration, #didn't work
            )

        if args.save and anim is not None: #only runs if a filename is given
            fps = max(1, int(round(1000 * args.speed / args.interval))) #fps calculation for?
            #remember, a video is just images playing at really fast fps, so this determines the speed of the video(the car moving basically)
            path = args.save
            if path.lower().endswith(".gif"): #arguments for a gif file
                anim.save(path, writer=matplotlib.animation.PillowWriter(fps=fps))
            else: #every other fil format
                anim.save(path, writer=matplotlib.animation.FFMpegWriter(fps=fps))
            print("Saved", path)
            plt.close("all")
    finally: #ensures log file is saved even if code crashes
        if log_stream is not None:
            log_stream.close()


if __name__ == "__main__": #tells computer to always run from main
    main()
