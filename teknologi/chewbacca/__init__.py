from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor
import time
import math

class Direction:
    LEFT = 0
    RIGHT = 1

class Chewbacca:
    LEFT = 0
    RIGHT = 1

    WHEEL_DIAMETER = 88.5
    WHEEL_DISTANSE = 98.4

    WHEEL_MAX_ROTATION_SPEED = 800 #grader pr sekund
    WHEEL_MAX_ACCELERATION = 400   #grader pr sekund   pr  sekund
    DRIVEBASE_MAX_SPEED = 620
    DRIVEBASE_MAX_ACCELERATION = 40
    DRIVEBASE_MAX_TURNRATE = 360
    DRIVEBASE_MAX_TURN_ACCELERATION = 360
    
    ACCELERATION = 500 #mm/s²
    MIN_DECELERATION_SPEED = 10 #mm/s

    PORT_RIGHT_MOTOR = Port.D
    PORT_LEFT_MOTOR = Port.A
    PORT_RIGHT_WORK_MOTOR = Port.B
    PORT_LEFT_WORK_MOTOR = Port.C

    RIGHT_COLOR_SENSOR = Port.S1
    LEFT_COLOR_SENSOR = Port.S3
    GYRO_SENSOR = Port.S4

    


    def __init__(self) -> None:
        self.brain = EV3Brick()
        self.motor_R = Motor(self.PORT_RIGHT_MOTOR)
        self.motor_L = Motor(self.PORT_LEFT_MOTOR)
        self.__motor_work_R__ = Motor(self.PORT_RIGHT_WORK_MOTOR)
        self.__motor_work_L__ = Motor(self.PORT_LEFT_WORK_MOTOR)
        self.__driveBase__ = DriveBase(self.motor_L, self.motor_R, self.WHEEL_DIAMETER, self.WHEEL_DISTANSE)
        # self.color_R = ColorSensor(self.RIGHT_COLOR_SENSOR)
        # self.color_L = ColorSensor(self.LEFT_COLOR_SENSOR)
        self.gyro = GyroSensor(self.GYRO_SENSOR)
        #self.motor_L.control.limits(Chewbacca.WHEEL_MAX_ROTATION_SPEED, Chewbacca.WHEEL_MAX_ACCELERATION, 100)
        #self.motor_R.control.limits(Chewbacca.WHEEL_MAX_ROTATION_SPEED, Chewbacca.WHEEL_MAX_ACCELERATION, 100)
        #self.__driveBase__.settings(Chewbacca.DRIVEBASE_MAX_SPEED, Chewbacca.DRIVEBASE_MAX_ACCELERATION, Chewbacca.DRIVEBASE_MAX_TURNRATE, Chewbacca.DRIVEBASE_MAX_TURN_ACCELERATION)


    def trippteller(self):
        Trippteller = self.motor_R + self.motor_L / 2
        return Trippteller



    def p_ctrl(self, target, current, kP):
        error = target - current
        controlSignal = kP * error

        return controlSignal

    def beep(self):
        self.brain.speaker.beep()
        wait(1000)


    def __get_dist_end_zone2__(speed, end_speed, target_distance):
        time_zone3 = (speed - end_speed) / Chewbacca.ACCELERATION
        average_speed_zone3 = (speed + end_speed) / 2
        dist_zone3 = average_speed_zone3 * time_zone3
        dist_end_zone2 = target_distance - dist_zone3
        return dist_end_zone2

    def __gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, distance, t0, acceleration_zone, t2):
        if acceleration_zone == 1:
            t1 = time.ticks_ms()
            t = (t1 - t0)/1000 #tid siden start i sekunder
            v = t * Chewbacca.ACCELERATION + start_speed
            if v >= speed:
                v = speed
                acceleration_zone = 2

        elif acceleration_zone == 2:
            v = speed
            if distance >= dist_end_zone2:
                t2 = time.ticks_ms()
                acceleration_zone = 3

        elif acceleration_zone == 3:
            t3 = time.ticks_ms()
            t = (t3 - t2)/1000 #tid siden start i sekunder 
            v = speed - Chewbacca.ACCELERATION * t
            if v <= Chewbacca.MIN_DECELERATION_SPEED:
                v = Chewbacca.MIN_DECELERATION_SPEED
        return (v, t2, acceleration_zone)


    # #Kjøre myke svinger
    # def drive_gyro_turn(self, start_speed, speed, end_speed, turn_radius, turn_angle, turn_right = True, stop_at_end = True, kP=1.0):
        
    #     if turn_right & (turn_angle >= 0) :
    #         turn_right = True
    #         turn_angle = turn_angle * 1
    #     elif turn_right & (turn_angle < 0) :
    #         turn_right = True
    #         turn_angle = turn_angle * -1
    #     elif turn_right & (turn_angle >= 0) :
    #         turn_right = False
    #         turn_angle = turn_angle * 1
    #     elif turn_right & (turn_angle < 0) :
    #         turn_right = False
    #         turn_angle = turn_angle * -1


    #     self.__driveBase__ = DriveBase(self.motor_L, self.motor_R, self.WHEEL_DIAMETER, self.WHEEL_DISTANSE)
    #     self.motor_R
    #     self.motor_L

    # gjør om kjørt avstand til hjul rotasjon i grader
    def __mm_to_deg__(self, dist):
        O = self.WHEEL_DIAMETER * math.pi
        result = (dist / O) * 360
        return result
    
    # gjør om hjul rotasjon i grader til kjørt avstand 
    def __deg_to_mm__(self, degrees):
        O = self.WHEEL_DIAMETER * math.pi
        dist = O * degrees / 360
        return dist

    def drive_gyro_turn(self, speed, turn_radius, turn_angle, turn_right = True, start_speed = 0, end_speed = 0, stop_at_end = True, kP=1.0):
        gyrovinkel0 = self.gyro.angle()
        
        # svingens retning vises i turn_right variabelen og turn_angle gjøres alltid positiv
        if turn_right & (turn_angle >= 0) :
            turn_right = True
            turn_angle = turn_angle * 1

        elif turn_right & (turn_angle < 0) :
            turn_right = False
            turn_angle = turn_angle * -1

        elif (turn_right == False) & (turn_angle >= 0) :
            turn_right = False
            turn_angle = turn_angle * 1

        elif (turn_right == False)  & (turn_angle < 0) :
             turn_right = True
             turn_angle = turn_angle * -1

        reached_goal = False

        #stopper drivebase når den har kontroll over motorene før vinkler resetes
        self.__driveBase__.stop()

        self.motor_R.reset_angle(0)
        self.motor_L.reset_angle(0)

        rygger = False
        if speed < 0:
            rygger = True
            speed = -1 * speed

        # regner ut hvor langt det ytteste hjulet skal kjøre
        dist1 = (turn_angle / 360) * 2 * math.pi * (turn_radius + (Chewbacca.WHEEL_DISTANSE / 2))
        # regner ut hvor langt det ytteste hjulet skal kjøre
        dist2 = (turn_angle / 360) * 2 * math.pi * (turn_radius - (Chewbacca.WHEEL_DISTANSE / 2))
        


        if dist1 < 0:
            rygger = True
            dist1 = -1 * dist1

        if start_speed < 0:
            start_speed = start_speed * -1 

        if end_speed < 0:
            end_speed = end_speed * -1 
        
        # gjør om hasighetene fra millimeter / sekund til grader / sekund
        start_speed = self.__mm_to_deg__(start_speed)
        end_speed = self.__mm_to_deg__(end_speed)
        speed = self.__mm_to_deg__(speed)

        #dette skal sjekke at det ikke er bedt om for høy fart
        v1 = math.sqrt(dist1 * self.__mm_to_deg__(Chewbacca.ACCELERATION) + 0.5*start_speed**2 + 0.5*end_speed**2)
        #print("v1 er regnet ut til :", v1)
        if speed > v1:
            speed = v1
        
        #setter end_speed ned hvis end_speed er høyere enn max fart
        if end_speed > v1:
            for i in range(end_speed, 0, -1):
                v1 = math.sqrt(dist1 * self.__mm_to_deg__(Chewbacca.ACCELERATION) + 0.5*start_speed**2 + 0.5*i**2)
                if i <= v1:
                    end_speed = i
                    break
        
        #setter start_speed ned hvis start_speed er høyere enn max fart
        if start_speed > v1:
            for i in range(start_speed, 0, -1):
                v1 = math.sqrt(dist1 * self.__mm_to_deg__(Chewbacca.ACCELERATION) + 0.5*i**2 + 0.5*end_speed**2)
                if i <= v1:
                    start_speed = i
                    break


        dist_end_zone2 = Chewbacca.__get_dist_end_zone2__(speed, end_speed, dist1)
        dist_end_zone2 = self.__mm_to_deg__(dist_end_zone2)
        acceleration_zone = 1

        t0 = time.ticks_ms()
        t2 = 0
        if (not rygger) & turn_right:
            #kjøres når du kjører fram til høyre
            while not reached_goal:
                gyrovinkel = self.gyro.angle() - gyrovinkel0
                #svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.motor_L.angle()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, distance, t0, acceleration_zone, t2)

                #self.__driveBase__.drive(v, svinge_hastighet)
                self.motor_L.run(v)
                self.motor_R.run(v * (dist2 / dist1))

                reached_goal = abs(gyrovinkel) >= turn_angle
                print(self.__deg_to_mm__(v))


        elif (not rygger) & (not turn_right):
            #kjøres når du kjører fram til venstre
            while not reached_goal:
                gyrovinkel = self.gyro.angle() - gyrovinkel0
                #svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.motor_R.angle()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, distance, t0, acceleration_zone, t2)

                #self.__driveBase__.drive(v, svinge_hastighet)
                self.motor_R.run(v)
                self.motor_L.run(v * (dist2 / dist1))

                reached_goal = abs(gyrovinkel) >= turn_angle
                print(self.__deg_to_mm__(v))
                


        elif rygger & turn_right:
            #kjøres når du kjører bak til høyre
            while not reached_goal:
                gyrovinkel = self.gyro.angle() - gyrovinkel0
                #svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.motor_L.angle()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, -distance, t0, acceleration_zone, t2)

                #self.__driveBase__.drive(v, svinge_hastighet)
                self.motor_L.run(-v)
                self.motor_R.run(-v * (dist2 / dist1))

                reached_goal = abs(gyrovinkel) >= turn_angle
               # print(acceleration_zone, -distance, v)
        
        elif rygger & (not turn_right):
            #kjøres når du kjører bak til venstre
            while not reached_goal:
                gyrovinkel = self.gyro.angle() - gyrovinkel0
                #svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.motor_R.angle()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, -distance, t0, acceleration_zone, t2)

                #self.__driveBase__.drive(v, svinge_hastighet)
                self.motor_R.run(-v)
                self.motor_L.run(-v * (dist2 / dist1))

                reached_goal = abs(gyrovinkel) >= turn_angle
                #print(acceleration_zone, distance, v)

        if stop_at_end == True:
            self.__driveBase__.stop()
            self.motor_L.hold()
            self.motor_R.hold()        
        #returner siste kjørte hastighet
        v = self.__deg_to_mm__(v)
        return v




    def drive_gyro_dist(self, speed, target_angle, target_distance, start_speed = 0, end_speed = 0, stop_at_end = True, kP=1.0):
        reached_goal = False
        self.__driveBase__.reset()

        rygger = False
        if speed < 0:
            rygger = True
            speed = -1 * speed

        if target_distance < 0:
            rygger = True
            target_distance = -1 * target_distance

        if start_speed < 0:
            start_speed = start_speed * -1 

        if end_speed < 0:
            end_speed = end_speed * -1 
        

        #dette skal sjekke at det ikke er bedt om for høy fart
        v1 = math.sqrt(target_distance * Chewbacca.ACCELERATION + 0.5*start_speed**2 + 0.5*end_speed**2)
        #print("v1 er regnet ut til :", v1)
        if speed > v1:
            speed = v1
        
        #setter end_speed ned hvis end_speed er høyere enn max fart
        if end_speed > v1:
            for i in range(end_speed, 0, -1):
                v1 = math.sqrt(target_distance * Chewbacca.ACCELERATION + 0.5*start_speed**2 + 0.5*i**2)
                if i <= v1:
                    end_speed = i
                    break
        
        #setter start_speed ned hvis start_speed er høyere enn max fart
        if start_speed > v1:
            for i in range(start_speed, 0, -1):
                v1 = math.sqrt(target_distance * Chewbacca.ACCELERATION + 0.5*i**2 + 0.5*end_speed**2)
                if i <= v1:
                    start_speed = i
                    break


        dist_end_zone2 = Chewbacca.__get_dist_end_zone2__(speed, end_speed, target_distance)
        acceleration_zone = 1

        t0 = time.ticks_ms()
        t2 = 0
        if not rygger:
            #kjøres når du ikke rygger
            while not reached_goal:
                gyrovinkel = self.gyro.angle()
                svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.__driveBase__.distance()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, distance, t0, acceleration_zone, t2)

                self.__driveBase__.drive(v, svinge_hastighet)

                reached_goal = distance >= target_distance
                print(v)


        else:
            #kjøres når du rygger
            while not reached_goal:
                gyrovinkel = self.gyro.angle()
                svinge_hastighet = (gyrovinkel - target_angle) * kP

                distance = self.__driveBase__.distance()

                (v, t2, acceleration_zone) = Chewbacca.__gets_speed_during_acceleration__(start_speed, speed, dist_end_zone2, -distance, t0, acceleration_zone, t2)

                self.__driveBase__.drive(v * -1, svinge_hastighet)

                reached_goal = distance <= target_distance * -1
                #print(acceleration_zone, distance, v)

        if stop_at_end == True:
            self.__driveBase__.stop()
            self.motor_L.hold()
            self.motor_R.hold()        
        #returner siste kjørte hastighet
        return v




    def line_follower(self, fargesensor: ColorSensor, driveBase: DriveBase, speed, kP, distance):
        while True:
            svart_hvit = 55
            lysstyrke = fargesensor.reflection()
            retning =  self.p_ctrl(svart_hvit, lysstyrke, kP)
            driveBase.drive(speed, retning)



    def work_motor_L(self, speed, target_rotation):
    
        self.__motor_work_L__.run_angle(speed, target_rotation)

    def work_motor_R(self,  speed, target_rotation):

        self.__motor_work_R__.run_angle(speed, target_rotation)

    def TestAvSide(self, side):
        if side == "right":
            print("rett")

        elif side == "left":
            print("galt")

        else:
            print("skjønte ikke hva du mente")

    def vri_grader(self, target_angle):
        self.__driveBase__.turn(-1 * target_angle)

    def straight(self, distance):
            self.__driveBase__.straight(distance)

    def gyro_svimmel(self):
        vinkelhastighet = self.gyro.speed()

        vinkelhastighet = abs(vinkelhastighet)

        if vinkelhastighet <= 1:
            self.brain.light.on(Color.GREEN)

        else:
            self.brain.light.on(Color.RED)

    def gyro_kalibrer(self):
        self.brain.light.on(Color.ORANGE)
        wait(1000)
        sensor = Ev3devSensor(Chewbacca.GYRO_SENSOR)
        sensor.read("GYRO-CAL")
        self.brain.light.on(Color.GREEN)

    
    def press_robot_frem(self, fart=45, kraft_L=30, kraft_R=30):
        
        self.forrige_limit = self.motor_L.control.limits()
        self.motor_L.control.limits(self.forrige_limit[0], self.forrige_limit[1], kraft_L)
        self.motor_R.control.limits(self.forrige_limit[0], self.forrige_limit[1], kraft_R)

        self.motor_L.run(fart) #grader pr sekund
        self.motor_R.run(fart) #grader pr sekund

    def press_robot_frem_ferdig(self):
        self.motor_L.stop()
        self.motor_R.stop()
        self.motor_L.control.limits(self.forrige_limit[0], self.forrige_limit[1], self.forrige_limit[2])
        self.motor_R.control.limits(self.forrige_limit[0], self.forrige_limit[1], self.forrige_limit[2])


