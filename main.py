#new update broke audio (not that we need)
from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from ursina import *
from cube_interface.cube import Cube
from cube_representation.cube_state import CubeState
import cube_interface.constants as constants

#create the app and enable camera
app = Ursina()
EditorCamera()

#init our cube and cube state
cube = Cube()
state = CubeState() 

def apply_move(move, speed):
    """Applies moves to the cube state and frontend."""

    cube.queue_move(move, speed)
    state.apply_move(move)

def scramble(n=20):
    """Scrambles the cube with 20 random moves."""

    for _ in range(n):
        apply_move(random.choice(constants.MOVES), constants.SCRAMBLE_SPEED)

def input(key):
    """Handles inputs."""

    shift = held_keys['shift']

    if key == 's':
        if shift:
            scramble()
        else:
            #SOLVE WILL GO HERE
            pass  
    elif key in constants.KEYS:
        #determine if prime and apply move
        move = constants.KEYS[key] + ("'" if shift else "")
        apply_move(move, constants.NORMAL_SPEED)






#run
app.run()