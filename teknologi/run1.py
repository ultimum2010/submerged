#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca

def run():
    global chewie
    chewie = Chewbacca()

    chewie.drive_gyro_dist(100, 0, 100  )
    chewie.drive_gyro_dist(100, -45, 500)

run()