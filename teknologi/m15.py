#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run():
    chewie = Chewbacca()
     
    #linjene under viser kjøring til lasteskip installasjonen
    chewie.drive_gyro_dist(start_speed= 0, speed= 250, end_speed= 0,
                           target_distance= 135, target_angle= 0,
                           stop_at_end= True)

    #linjen under viser roteringen på samlebåndet
    chewie.work_motor_R(speed=-500, target_rotation=1000)
    
    #linjene under viser returnering til det røde hjemområdet 
    chewie.drive_gyro_dist(start_speed= 0, speed= 250, end_speed= 0,
                           target_distance= -135, target_angle= 0,
                           stop_at_end= True)
    
    # chewie.work_motor_R(speed= -500, target_rotation= 250)

   