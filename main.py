#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()
# Initialize a motor at port A og D.
A = Motor(port=Port.A)
B = Motor(port=Port.B)
#Initialize the sensors.
us = UltrasonicSensor(port=Port.S1)
colorSensorV = ColorSensor(port=Port.S2)
colorSensorH = ColorSensor(port=Port.S3)
touch = TouchSensor(port=Port.S4)
#RED = 20
#GREEN = 20
#BLUE = 30
robot = DriveBase(A, B, wheel_diameter=56, axle_track=130)
arr = []
start = True
startag = False
while(start):
    (RED, GREEN, BLUE) = colorSensorV.rgb()
    RED -=5
    GREEN -=5
    BLUE -=20
    t_1 = 0
    t_2 = 0
    print(str(RED) + " " + str(GREEN) + " " + str(BLUE))
    if(touch.pressed()):
        startag = True
    while(startag):
        if us.distance() > 100:
            (red, green, blue) = colorSensorV.rgb()
            is_black = red < RED or green < GREEN or blue < BLUE
            (red1, green1, blue1) = colorSensorH.rgb()
            is_black2 = red1 < RED or green1 < GREEN or blue1 < BLUE
            print(colorSensorV.rgb())
            print(colorSensorH.rgb())
            robot.drive(150,0)
            if(is_black):
                robot.drive(25,70)
                if(time.time()-t_2 < 0.5):
                    robot.stop()
                    robot.turn(25)
                    robot.straight(100)
                t_1 = time.time()
            elif(is_black2):
                robot.drive(25,-70)
                if(time.time()-t_1 < 0.5):
                    robot.stop()
                    robot.turn(-25)
                    robot.straight(100)
                t_2 = time.time()
            t_1 = 0 
            t_2 = 0
        else:
            robot.stop()
