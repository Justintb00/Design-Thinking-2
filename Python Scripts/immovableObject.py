#!/usr/bin/env python3
#By: Paola Camacho#

DISTANCE_THRESHOLD=1  # distance in inches in which an object is acknowledged to exist
STARTING_SPEED = 50

import traceback
import picar
from picar.obstacle_sensor import *
from picar.front_wheels import *
from picar.back_wheels import *
from picar.line_sensor import *
import time

steering = Front_Wheels()  # create a Front_Wheels object for steering the car
motors = Back_Wheels()    # create a Back_Wheels object to move the car
objSensor = Obstacle_Sensor()  # create an Object_Sensor() object to detect distance to objects
lineSensor = Line_Sensor() # create a Line_Sensor() object to detect line

picar.setup()
steering.ready()
motors.speed = STARTING_SPEED
motors.ready()

def isObjectDetected(within_a_distance):
    within_a_distance = within_a_distance*2.54
    read1 = objSensor.distance()
    read2 = objSensor.distance()
    read3 = objSensor.distance()
    averageOf3 = (read1+read2+read3)/3
    if (averageOf3 <= within_a_distance):
        return True
    else:
        return False

    return averageOf3

def avoidImmovableObject():
    motors.stop()
    #TURN RIGHT
    if readLine in [[1,0,0,0,0],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0]]:
        steering.turn_right()
        motors.forward()
        time.sleep(2)
    #TURN LEFT
    if readLine in [[0,0,0,0,1],[0,0,0,1,1],[0,0,1,1,1],[0,1,1,1,1]]:
        steering.turn_left()
        motors.forward()
        time.sleep(2)
        


def goBotImmovableObject():
    motors.forward()
    try:
        while True:
            if isObjectDetected(DISTANCE_THRESHOLD):
                avoidImmovableObject();
    except:
        motors.stop()
        steering.ready()
