#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)
x_motor = Motor(Port.B)
y_motor = Motor(Port.A)
z_motor = Motor(Port.C)

# Write your program here.
ev3.speaker.beep()

a = open('some_text.txt', 'r')
opened_file = a.read()
a.close()
l = opened_file.split('\n')
robot_list = []
for y in range(len(l)):
    l1 = l[y].split(' ')
    l1.pop(-1)
    robot_list.append(l1)
robot_list.pop(-1)
for y in range(len(robot_list)):
    for x in range(len(robot_list[y])):
        robot_list[y][x] = int(robot_list[y][x])

while not color_sensor.reflection() > 40:
    y_motor.dc(50)
y_motor.brake()

while not touch_sensor.pressed():
    x_motor.dc(50)
x_motor.brake()
y_motor.brake()

x_motor.reset_angle(0)
y_motor.reset_angle(0)
z_motor.reset_angle(0)

def v1():
    for y in range(len(robot_list)):
        while not touch_sensor.pressed():
            x_motor.dc(50)
        for i in range(5):
            x_motor.brake()
            y_motor.brake()
            z_motor.brake()
        for x in range(len(robot_list[y])):
            if robot_list[y][x] == 0:
                z_motor.reset_angle(0)
                while abs(z_motor.angle()) < 159: # 180
                    z_motor.dc(50)
                for i in range(5):
                    x_motor.brake()
                    y_motor.brake()
                    z_motor.brake()
                while abs(x_motor.angle()) // 8.2 < x:
                    x_motor.dc(-50)
                for i in range(5):
                    x_motor.brake()
                    y_motor.brake()
                    z_motor.brake()
                z_motor.reset_angle(0)
                while abs(z_motor.angle()) < 159: # 180
                    z_motor.dc(50)
                for i in range(5):
                    x_motor.brake()
                    y_motor.brake()
                    z_motor.brake()
        while abs(y_motor.angle()) // 8.2 < y:
            y_motor.dc(50)
        for i in range(5):
            x_motor.brake()
            y_motor.brake()
            z_motor.brake()

def v2():
    x_motor.reset_angle(0)
    y_motor.reset_angle(0)
    z_motor.reset_angle(0)
    last_color = None
    for y in range(len(robot_list)):
        robot_list[y].reverse()
    for y in range(len(robot_list)):
        while not touch_sensor.pressed():
            x_motor.dc(50)
        for i in range(5):
            x_motor.brake()
            y_motor.brake()
            z_motor.brake()
        for x in range(len(robot_list[y])):
            if robot_list[y][x] == 0:
                while z_motor.angle() < 180:
                    z_motor.dc(40)
                for i in range(5):
                    z_motor.brake()
            else:
                while z_motor.angle() > 0:
                    z_motor.dc(-40)
                for i in range(5):
                    z_motor.brake()
            # wait(100)
            while abs(x_motor.angle()) < x * 8.2:
                x_motor.dc(-50)
            for i in range(5):
                x_motor.brake()
            last_color = robot_list[y][x]
            # wait(100)
        while z_motor.angle() > 0:
            z_motor.dc(-40)
        for i in range(5):
            z_motor.brake()
        while abs(y_motor.angle()) < y * 4.1:
            y_motor.dc(40)
        for i in range(5):
            x_motor.brake()
            y_motor.brake()
            z_motor.brake()
        print('INFO: ' + str(abs(y_motor.angle())) + ' y: ' + str(y))

v2()

for i in range(3):
    ev3.speaker.beep(400 + i * 100)

# for i in range(100):
#     z_motor.reset_angle(0)
#     while abs(z_motor.angle()) < 159:
#         z_motor.dc(50)

# battery: 6.90 V

# 838
# 840
# 843
# 837    --> 840
# 840
# 844
# 838
#                 --> 840 # 840 degrees = width of the A4 list
# 840
# 841
# 838
# 838    --> 840.285714286
# 842
# 839
# 844
