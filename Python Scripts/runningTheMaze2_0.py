#---By: Humberto (Alex) Trejo Galvan---#
STARTING_SPEED = 70

import traceback
import picar
from picar.front_wheels import *
from picar.back_wheels import *
from picar.line_sensor import *
import time

steering = Front_Wheels()  # create a Front_Wheels object for steering the car
motors = Back_Wheels()    # create a Back_Wheels object to move the car
lineSensor = Line_Sensor() # create a Line_Sensor() object to detect lines on the floor

picar.setup()
steering.ready()
motors.speed = STARTING_SPEED
motors.ready()



def getLineControls():

    lineSensor.read_digital()
    speed = motors.speed
    steeringAngle = steering.angle
              
    if lineSensor.read_digital() == [0,0,1,1,1]:
        speed = 20
        steeringAngle = 90
        
    else:
        speed = 30
        steeringAngle = 45

    return (speed,steeringAngle)        
        
def followLine():

    motors.forward()
    speed = motors.speed
    speed,steeringAngle = getLineControls()
    steering.turn(steeringAngle)
    time.sleep(0.5)
    motors.stop()
    #steering.ready()
    

def seekWall():

    motors.speed = 35

    while lineSensor.read_digital() == [0,0,0,0,0]:

        lineSensor.read_digital()
        steering.turn(135)
        motors.forward()

    motors.stop()


def maze():
    SEEK_WALL = 0
    ON_WALL = 1
    currentState = SEEK_WALL

    motors.speed = 50

    if currentState == SEEK_WALL:
        seekWall()
        currentState = ON_WALL

    if currentState == ON_WALL:

        print("here")
        
        lineSensor.read_digital()


        if lineSensor.read_digital() == [0,0,0,0,0]:
            currentState = SEEK_WALL

        if lineSensor.read_digital() == [1,1,1,1,1]:
            motors.stop()
            motors.backward()
            time.sleep(1.5)
            motors.stop()
            steering.turn(50)
            motors.forward()
            time.sleep(1)
            currentState = SEEK_WALL

        else:
            followLine()
            currentState = SEEK_WALL
