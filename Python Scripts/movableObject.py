#By: Justin Bennett#
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

def determineMovable():
    read1 = objSensor.distance()
    steering.turn(90)
    time.sleep(.1)
    motors.forward()
    time.sleep(.5)
    motors.backward()
    time.sleep(.5)
    motors.stop()
    steering.turn(90)
    read2 = objSensor.distance()
    if abs(read2 - read1) > 1:
        return True
    return False
