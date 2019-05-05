STARTING_SPEED = 50

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
    
    onLine = [[0,0,0,1,1],[0,0,1,1,1]]
    rLine = [[0,0,0,0,1], [0,0,0,1,0],[0,0,1,1,0],[0,1,1,1,1]]
    lLine = [[1,1,1,1,0],[0,1,1,0,0],[0,1,1,1,0],[0,1,0,0,0],[1,1,0,0,0],[1,1,1,0,0]]
              
    if lineSensor.read_digital() in onLine:
        speed = 10
        steeringAngle = 90
        
    elif lineSensor.read_digital() in rLine:
        speed = 10
        steeringAngle = 50
        
    elif lineSensor.read_digital() in lLine:
        speed = 10
        steeringAngle = 100

    elif lineSensor.read_digital() == [0,0,0,0,0]:
        speed = 10
        steeringAngle = 110

    return (speed,steeringAngle)        
        
def followLine():

    motors.forward()
    speed = motors.speed
    speed,steeringAngle = getLineControls()
    steering.turn(steeringAngle)
    time.sleep(0.3)
    motors.stop()
    steering.ready()
    
def testLineSensor():
    try:
        while True:
            print('Line Sensor values:',lineSensor.read_digital())
    except:
        pass

def goBot():
    try:
        followLine()
    except Exception as e:
        traceback.print_exc()
    finally:
        motors.stop()
        steering.ready()

def seekWall():

    print("SEEK_WALL")

    lineSensor.read_digital()

    if lineSensor.read_digital() == [0,0,0,0,0]:
        steering.turn(110)
        motors.forward()

    elif lineSensor.read_digital() == [1,1,0,0,0] or lineSensor.read_digital() == [1,0,0,0,0] or lineSensor.read_digital() == [1,1,1,0,0] or lineSensor.read_digital() == [1,1,1,1,0]:
        steering.turn(70)
        motors.backward()

def maze():
    
    SEEK_WALL = 0
    ON_WALL = 1
    currentState = SEEK_WALL

    while True:

        motors.speed = 35

        if currentState == SEEK_WALL:
            seekWall()
            currentState = ON_WALL

        elif currentState == ON_WALL:

            print("ON_WALL")
            
            lineSensor.read_digital()
            print(lineSensor.read_digital())

            if lineSensor.read_digital() == [1,1,1,1,1] or lineSensor.read_digital() == [1,1,1,1,0] or lineSensor.read_digital() == [0,1,1,1,1]:
                motors.backward()
                time.sleep(1.5)
                motors.stop()
                steering.turn(70)
                motors.forward()
                time.sleep(1)
                currentState = SEEK_WALL

            elif lineSensor.read_digital() == [0,0,0,0,0]:
                currentState = SEEK_WALL

            else:
                goBot()
