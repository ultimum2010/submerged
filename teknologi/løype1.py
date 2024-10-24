#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run():
    chewie = Chewbacca()
     

    fast = 300
    slow = 75
    v = chewie.drive_gyro_dist(start_speed= 0, speed= slow, end_speed= 0,
                               target_distance= 700, target_angle= 0,
                               stop_at_end= True)
    
    v = chewie.drive_gyro_dist(start_speed= 0, speed= slow, end_speed= 0,
                               target_distance= -700, target_angle= 0,
                               stop_at_end= True)
    
    # v = chewie.drive_gyro_turn(start_speed= v, speed= slow, end_speed= slow, 
    #                            turn_radius= 0, turn_angle= -160,
    #                            stop_at_end= False)
    
    # v = chewie.drive_gyro_dist(start_speed= v, speed= fast, end_speed= fast,
    #                            target_distance= 600, target_angle= 180,
    #                            stop_at_end= False)
    
    # v = chewie.drive_gyro_turn(start_speed= v, speed= fast, end_speed= slow, 
    #                            turn_radius= 150, turn_angle= 270,
    #                            stop_at_end= False)
    
    # v   = chewie.drive_gyro_dist(start_speed= v, speed= slow, end_speed= 0,
    #                            target_distance= 100, target_angle= -90,
    #                            stop_at_end= True)

 
