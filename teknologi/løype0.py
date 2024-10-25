#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time


def run():
    chewie = Chewbacca()
     
    v = chewie.drive_gyro_dist(start_speed= 0, speed= 300, end_speed= 300,
                               target_distance= 95, target_angle= 0,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 300, end_speed= 300, 
                               turn_radius= 250, turn_angle= 70,
                               stop_at_end= False)
    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 300, end_speed= 0,
                               target_distance= 202, target_angle= 80,
                               stop_at_end= True)
    
    chewie.work_motor_L(speed= -500, target_rotation= 250)

    chewie.motor_L.run_angle(40, -10)  #Venstre hjul litt bak
    chewie.work_motor_L(speed= -500, target_rotation= 1055)

    #time.sleep(1)

    v = chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                               target_distance= -110, target_angle= 90,
                               stop_at_end= True)


    v = chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 100, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -80,
                               stop_at_end= True)

    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 100,
                               target_distance= 120, target_angle= 0,
                               stop_at_end= True)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 100, end_speed= 0, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -82,
                               stop_at_end= True)

    # snur korallknoppende opp (M01)
    v = chewie.drive_gyro_dist(start_speed= v, speed= 70, end_speed= 0,
                               target_distance= 68, target_angle= -90,
                               stop_at_end= False)
    

    v = chewie.drive_gyro_dist(start_speed= v, speed= -100, end_speed= 0,
                               target_distance= 170, target_angle= -90,
                               stop_at_end= True)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 100, end_speed= 0, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= 35,
                               stop_at_end= True, turn_right= True)


    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
                               target_distance= 215, target_angle= -50,
                               stop_at_end= True)
    
    chewie.work_motor_L(speed= 500, target_rotation= 1330)
 
