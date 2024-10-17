#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run():
    chewie = Chewbacca()

    v = chewie.drive_gyro_dist(start_speed= 0, speed= 150, end_speed= 150,
                               target_distance= 111, target_angle= 0,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 150, end_speed= 150, 
                               turn_radius= 250, turn_angle= 75,
                               stop_at_end= False)
    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 400, end_speed= 0,
                               target_distance= 173, target_angle= -79,
                               stop_at_end= True)
    
    
    
    # v = chewie.drive_gyro_turn(start_speed= 0, speed= 300, end_speed= 300, 
    #                            turn_radius= 300, turn_angle= 55,
    #                            turn_right= True,  stop_at_end= False)
    
    # v = chewie.drive_gyro_dist(start_speed= v, speed= 300, end_speed= 0,
    #                            target_distance= 290, target_angle= -67,
    #                            stop_at_end= True)
    
    chewie.work_motor_L(speed= -800, target_rotation= 1310)
    chewie.work_motor_L(speed= 800, target_rotation= 1310)


