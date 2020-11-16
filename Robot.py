#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

class Robot:
    # Konstruktør
    def __init__(self):
        self.motor_plate = Motor(port=Port.C)
        self.motor_1 = Motor(port=Port.B)
        self.motor_2 = Motor(port=Port.A)
        self.touch_left = TouchSensor(port=Port.S1)
        self.touch_right = TouchSensor(port=Port.S2)

    # metode som roterer plate etter input av speed
    def rotatePlate(self,speed=0):
        self.motor_plate.run(speed)

    # Metode som roterer motorer etter input av speed_1 og speed_2
    def rotateMotors(self,speed_m1=0, speed_m2=0):
        self.motor_1.run(speed=speed_m1)
        self.motor_2.run(speed=speed_m2)

    def stopMotors(self):
        self.motor_1.stop()
        self.motor_2.stop()
        self.motor_plate.stop()

    def case_1(self):
        n_time = time.time()
        time_limit = 20
        while(time.time()-n_time <= time_limit):
            obj.rotateMotors(200,400)
            obj.rotatePlate(60)
        obj.stopMotors()    
        return True

    def case_2(self):
        n_time = time.time()
        time_limit = 30
        while(time.time()-n_time <= time_limit):
            obj.rotateMotors(200,0)
            obj.rotatePlate(200)
        obj.stopMotors()   
        return True

    def case_3(self):
        n_time = time.time()
        time_limit = 20
        while(time.time()-n_time <= time_limit + 10):
            obj.rotateMotors(1560,0)
            obj.rotatePlate(700)
            while(time.time() - n_time <= time_limit):
                obj.rotateMotors(1200,0)
                obj.rotatePlate(1500)
            
        obj.stopMotors()    
        return True
      
    def case_4(self):
        n_time = time.time()
        time_limit = 15
        while(time.time()-n_time <= time_limit):
            while(time.time() - n_time<=7):
                obj.rotateMotors(200,50)
                obj.rotatePlate(150)
            while(time.time()- n_time <= 15):
                obj.rotateMotors(-100, -200)
                obj.rotatePlate(-150)
        obj.stopMotors()    
        return True

    def case_5(self):
        n_time = time.time()
        time_limit = 15
        while(time.time()-n_time <= time_limit + 3):
            wait(100)
            obj.rotateMotors(0,45)
            obj.rotatePlate(500)
            while(time.time()-n_time <= time_limit):
                obj.rotateMotors(1000,0)
                obj.rotatePlate(1200)
        obj.stopMotors()    
        return True
      

    def switch(self, i):
        default = "Program doesnt exist"
        return getattr(self, 'case_' + str(i), lambda: default)()
    

    def main(self):
        nr = 1
        while(True):
            ev3.screen.print(nr)
            if(self.touch_left.pressed()):
                wait(500)
                nr+=1
                if(nr>5):
                    nr=1
            if(self.touch_right.pressed()):
                wait(500)
                obj.switch(nr)
                nr+=1
                if(nr>5):
                    nr=1
                

ev3 = EV3Brick()
obj = Robot()
obj.main()
