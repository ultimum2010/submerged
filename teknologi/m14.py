#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time

def run():
    global che
    che = Chewbacca()
    #starter med å svinge til venstre mot reke 67 grader med 265 mm per sekund og 200 mm. 
    che.drive_gyro_dist(265, 67, 200)
    #kjører 230 mm rett frem
    che.drive_gyro_dist(250,0,230)
    che.drive_gyro_dist(250,0,200)
    che.drive_gyro_dist(190,60,0)
    #che.drive_gyro_dist(100, -60, 490)
    #che.work_motor_L(600, -1300)
    
run()