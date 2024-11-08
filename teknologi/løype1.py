#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time



def run():
    #Kjør til M08 - Kunstig habitat
    #Start 8 tommer fra kanten i sør med front mot vest. Bruk verktøy for å sette nøyaktig avstand
    #Pass på at habitatet ligger på linjen slik det skal

    chewie = Chewbacca()

    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 100, 
                           turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -40,
                           stop_at_end= False)

    chewie.drive_gyro_dist(start_speed= 100, speed= 250, end_speed= 0,
                           target_distance= 320, target_angle= -45,
                           stop_at_end= True)
    
    chewie.vri_til_retning(32)

    chewie.work_motor_L(speed=-360, target_rotation=478)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 70, target_angle= 32,
                           stop_at_end= True)
    
    #For å være sikker på hvor roboten er så presser vi den mot intallasjonen og trekker den tilbake 15mm
    chewie.press_robot_frem()
    time.sleep(.5)
    chewie.press_robot_frem_ferdig()
    chewie.drive_gyro_dist(start_speed= 0, speed= 50, end_speed= 0,
                           target_distance= -5, target_angle= 32,
                           stop_at_end= True)  

    # # M13 Løft vri senk
    chewie.work_motor_L(speed=360, target_rotation=150)
    chewie.drive_gyro_turn(speed=100, turn_radius=0, turn_angle=20)
    chewie.work_motor_L(speed=360, target_rotation=-150)



    #Rygg bort fra installasjonen og løft verktøyet
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= -40, target_angle= 32,
                           stop_at_end= True) 
    chewie.work_motor_L(speed=360, target_rotation=500)  #Verktøyet helt opp
     

    chewie.vri_til_retning(-10)
    chewie.drive_gyro_dist(start_speed= 0, speed= 300, end_speed= 0,
                           target_distance= 350, target_angle= -10,
                           stop_at_end= True)
    
    chewie.drive_gyro_turn(start_speed= 0, speed= 150, end_speed= 0, 
                           turn_radius= 0, turn_angle= 80,
                           stop_at_end= True)
    

    #Verktøy ned for å gjøre M14 - Innsamling av prøver
    chewie.work_motor_L(speed=-360, target_rotation=450)

    chewie.drive_gyro_dist(start_speed= 0, speed= 50, end_speed= 0,
                           target_distance= 46, target_angle= 73,
                           stop_at_end= True)
    
    chewie.work_motor_L(speed=-100, target_rotation= 120)

    chewie.drive_gyro_dist(start_speed= 0, speed= 50, end_speed= 0,
                           target_distance= -60, target_angle= 75,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 50, end_speed= 0,
                           target_distance= 34, target_angle= 75,
                           stop_at_end= True)

    chewie.work_motor_L(speed=-100, target_rotation= -300)

    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 0, 
                           turn_radius= 0, turn_angle= -150,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 200, end_speed= 0,
                           target_distance= 515, target_angle= -90,
                           stop_at_end= True)
    
    chewie.drive_gyro_turn(start_speed= 0, speed= 50, end_speed= 0, 
                           turn_radius= 0, turn_angle= 20,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 150, end_speed= 0,
                           target_distance= 300, target_angle= -70,
                           stop_at_end= True)
    
    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 100, 
                           turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -30,
                           stop_at_end= True)

    chewie.drive_gyro_dist(start_speed= 0, speed= 150, end_speed= 0,
                           target_distance= 200, target_angle= -100,
                           stop_at_end= False)

    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 100, 
                           turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -30,
                           stop_at_end= False)

    chewie.drive_gyro_dist(start_speed= 0, speed= 350, end_speed= 0,
                           target_distance= 800, target_angle= -150,
                           stop_at_end= True)
    return

    chewie.drive_gyro_turn(start_speed= 250, speed= 250, end_speed= 250, 
                           turn_radius= 150, turn_angle= 90,
                           stop_at_end= False)
    
    chewie.drive_gyro_dist(start_speed= 250, speed= 250, end_speed= 0,
                           target_distance= 100, target_angle= 40,
                           stop_at_end= True)
    



    return



    chewie.drive_gyro_dist(start_speed= 250, speed= 250, end_speed= 0,
                           target_distance= 165, target_angle= -115,
                           stop_at_end= True, kP=2)
    

    #Vri roboten til høyre og flytt de to ytterste delene og kom så litt frem for å presse dem på plass
    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 0, 
                           turn_radius= 0, turn_angle= 35,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 60, target_angle= -90,
                           stop_at_end= True)
    

    #Vri roboten litt bort fra habitatene, rygg og kom frem for å løfte habitatene med plogen
    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 0, 
                           turn_radius= 0, turn_angle= 10,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= -70, target_angle= -40,
                           stop_at_end= True)
    
    chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 0, 
                           turn_radius= 0, turn_angle= -50,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 200, target_angle= -90,
                           stop_at_end= True)
    
    
    
    #Nå står habitatene i en stabel to høy og to bred
    # Rygg senk verktøyet og kom frem for å tippe stabelen   
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= -140, target_angle= -90,
                           stop_at_end= True)
    
    chewie.work_motor_L(speed=-360, target_rotation=380)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 130, target_angle= -90,
                           stop_at_end= True)
    
    

    #Toppen har ramlet ned men ligger litt skjevt. Rygg bak til høyre og venstre og kjør så frem for å rette de skjeve habitatene
    chewie.drive_gyro_dist(start_speed= 0, speed= -100, end_speed= -100,
                           target_distance= -30, target_angle= -90,
                           stop_at_end= False)    
    chewie.drive_gyro_turn(start_speed= -100, speed= -100, end_speed= -100, 
                           turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= 30,
                           stop_at_end= False)
    chewie.drive_gyro_dist(start_speed= -100, speed= -100, end_speed= -100,
                           target_distance= -75, target_angle= -120,
                           stop_at_end= False)
    chewie.drive_gyro_turn(start_speed= -100, speed= -100, end_speed= 0, 
                           turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -30,
                           stop_at_end= True)
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 220, target_angle= -90,
                           stop_at_end= True)  
    
    
    #Tre habitater skal nå ligge korrekt. Løft armen, rygg, senk armen og snu den siste delen
    chewie.work_motor_L(speed=-360, target_rotation=-100) #Løft verktøyet så det ikke treffer installasjonen
    
    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= -100, target_angle= -90,
                           stop_at_end= True)

    chewie.work_motor_L(speed=-360, target_rotation=100) #Senk verktøyet 

    chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                           target_distance= 100, target_angle= -90,
                           stop_at_end= True)
    

    #Alt på plass. Løft armen og rygg hjem
    chewie.work_motor_L(speed=-360, target_rotation=-380) #Løft verktøyet rett opp
    chewie.drive_gyro_dist(start_speed= 0, speed= 350, end_speed= 0,
                           target_distance= -550, target_angle= -70,
                           stop_at_end= True)
 
