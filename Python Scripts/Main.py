from runningTheMaze2_0 import *
from immovableObject import *
from checkCommands import *
from PictureCommunication import *
from picar.back_wheels import *
from music import *
from movableObject import *


def main():
    motors = Back_Wheels()

    FOUND_MOOB = False

    DISTANCE_THRESHOLD=2

    #SEEK_WALL = 0
    #ON_WALL = 1
    #wallState = SEEK_WALL

    NO_OBSTACLE = False
    OBSTACLE = True

    currentState = NO_OBSTACLE
    

    while not FOUND_MOOB:

        if currentState == NO_OBSTACLE:
            maze()
            currentState = isObjectDetected(DISTANCE_THRESHOLD)
                
        elif currentState == OBSTACLE:
            
            motors.stop()
            TakePicture()
            x = RecievingCommand()
            
            if x == "immovable":
                motors.backward()
                time.sleep(.3)
                motors.stop()
                goBotImmovableObject()
                currentState = NO_OBSTACLE

            elif x == "movable":
                if determineMovable() == True:
                    print("Move the object")
                    time.sleep(3)
                else:
                    goBotImmovableObject()
                currentState = NO_OBSTACLE

            elif x == "sample":
                currentState = NO_OBSTACLE
                sampleFoundSound()
                
            elif x == 'moob':
                FOUND_MOOB = True
                moobSound()
                
            else:
                currentState = OBSTACLE
                
main()
