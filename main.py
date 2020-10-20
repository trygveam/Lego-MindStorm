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
RED = 10
GREEN = 10
BLUE = 20
robot = DriveBase(A, B, wheel_diameter=56, axle_track=130)
start = True
startag = False
while(start):
    if(touch.pressed()):
        startag = True
    while(startag):
        print(colorSensorH.rgb())
        print(colorSensorV.rgb())
        (red, green, blue) = colorSensorV.rgb()
        is_black = red < RED or green < GREEN or blue < BLUE
        (red1, green1, blue1) = colorSensorH.rgb()
        is_black2 = red1 < RED or green1 < GREEN or blue1 < BLUE
        if not (is_black or is_black2):
            robot.drive(200,0)
        elif(is_black):
            robot.drive(120,90)
        elif(is_black2):
            robot.drive(120,-90)
        else:
            robot.stop()
