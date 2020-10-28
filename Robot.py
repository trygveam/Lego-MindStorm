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
    def init(self):
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


    def first_program(self,input_time):
        n_time = time.time()
        while(time.time()-n_time <= input_time):
            obj.rotateMotors(200,0)
            obj.rotatePlate(200)

    def second_program(self,input_time):
    def third_program(self,input_time):
    def fourth_program(self,input_time):
    def fifth_program(self,input_time):

    def switch(self,i):
        switcher = {
            0:first_program,
            1:second_program,
            2:third_program,
            3:fourth_program,
            4:fifth_program
        }
        func = switcher.get(i, lambda:"invalid")
        obj.func()

    def main(self):
        nr = 0
        while(True):
            ev3.screen.print(nr)
            ev3.speaker.say(nr)
            if(self.touch_left.pressed()):
                wait(2000)
                nr+=1
            if(self.touch_right.pressed()):
                obj.switch(nr)


ev3 = EV3Brick()
obj = Robot()
obj.main()
