#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time

def run():
    global chewie
    chewie = Chewbacca()
    
    chewie.drive_gyro_dist(300, 0, 50)
    chewie.drive_gyro_dist(100, -60, 490)
    chewie.work_motor_L(600, -1300)
    
run(