#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time

def run():
    global chewie
    chewie = Chewbacca()
    
    chewie.drive_gyro_dist(150, 0, 50)
    chewie.drive_gyro_dist(100, -60, 490)
    qwerty = chewie.drive_gyro_dist(300, 0, 600, 0, 300, False, 2)
    qwerty = chewie.drive_gyro_dist(500, 0, 600, qwerty, 0, True, 2)
    #chewie.work_motor_L(600, -1300)
    #time.sleep(5)
    print("det som kom ut bak: ", qwerty)
    
run()