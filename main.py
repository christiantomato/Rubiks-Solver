#new update broke audio (not that we need)
from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from ursina import *
from cube_interface.cube import Cube
from cube_representation.cube_state import CubeState
from cube_representation.cube_orientation import CubeOrientation
import cube_interface.constants as interface_constants
import cube_representation.constants as representation_constants

#create the app and enable camera
app = Ursina()
EditorCamera()

#init our cube, cube state, and orientation tracker
cube = Cube()
state = CubeState()
orientation = CubeOrientation()

def apply_move(move, speed):
    """
    Applies moves to the cube state and frontend.
    
    Args: 
        move (str): The move. 
        speed (float): The animation speed.
    """

    cube.queue_move(move, speed)
    state.apply_move(orientation.translate(move))

    #test internal representation
    print(state.permutations)
    print(state.orientations)
    print("\n")

def scramble(n=20):
    """Scrambles the cube with 20 random moves."""

    for _ in range(n):
        apply_move(random.choice(representation_constants.MOVES), interface_constants.SCRAMBLE_SPEED)

def input(key):
    """Handles inputs."""

    shift = held_keys['shift']

    if key == 's':
        if shift:
            scramble()
        else:
            #SOLVE WILL GO HERE
            pass  
    elif key in interface_constants.KEYS:
        #determine if prime and apply move
        move = interface_constants.KEYS[key] + ("'" if shift else "")
        apply_move(move, interface_constants.NORMAL_SPEED)

#run
app.run()