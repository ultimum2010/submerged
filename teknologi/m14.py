#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time

def run():
    global che
    che = Chewbacca()
    
    #starter med å svinge til venstre mot krill 67 grader med 265 mm per sekund og 200 mm. 
    v = che.drive_gyro_dist(start_speed= 0, speed= 265, end_speed= 250,
                            target_distance= 200, target_angle= -80,
                            stop_at_end= False)
    
    #kjører 230 mm rett frem
    v = che.drive_gyro_dist(start_speed= 250, speed=250, end_speed= 250,
                            target_distance=230, target_angle= -20,
                            stop_at_end= False)
    #kjører 200 mm rett frem
    v = che.drive_gyro_dist(start_speed= 250, speed=250, end_speed=0,
                            target_distance=210, target_angle= -15,
                            stop_at_end= True)
    
    #svinger 6o grader til høyre
    # che.drive_gyro_dist(190,-60,0)
    # v = che.drive_gyro_dist(start_speed= 190, speed=250, end_speed= 190,
    #                         target_distance=210, target_angle= -60,
    #                         stop_at_end= False)
    
    # #che.work_motor_L(200,-65,190)
    # #che.drive_gyro_dist(100, -60, 490)
    # #che.work_motor_L(600, -1300)
    # che.drive_gyro_turn(speed=200,turn_radius=50,turn_angle=80, turn_right=True, start_speed=200)
    # che.work_motor_L(100,-400)
