#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run():
    chewie = Chewbacca()
     
    v = chewie.drive_gyro_dist(start_speed= 0, speed= 300, end_speed= 300,
                               target_distance= 95, target_angle= 0,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 300, end_speed= 300, 
                               turn_radius= 250, turn_angle= 70,
                               stop_at_end= False)
    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 300, end_speed= 0,
                               target_distance= 192, target_angle= 80,
                               stop_at_end= True)
    
    chewie.work_motor_L(speed= -500, target_rotation= 250)

    chewie.motor_L.run_angle(40, -10)  #Venstre hjul litt bak
    chewie.work_motor_L(speed= -500, target_rotation= 1080)

    v = chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                               target_distance= -100, target_angle= 90,
                               stop_at_end= True)

    chewie.work_motor_L(speed= 500, target_rotation= 1330)




    # v = chewie.drive_gyro_dist(start_speed= v, speed= 200, end_speed= 0,
    #                            target_distance= -200, target_angle= -79,
    #                            stop_at_end= True)
    

 
