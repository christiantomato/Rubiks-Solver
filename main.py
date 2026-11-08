#(audio is just breaking everything)
from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from ursina import *
from cube_interface.cube import Cube
from cube_representation.cube_state import CubeState
from cube_representation.cube_orientation import CubeOrientation
import cube_interface.constants as interface_constants
import cube_representation.constants as representation_constants

#init our frontend cube, cube state, and orientation tracker
cube = Cube()
state = CubeState()
orientation = CubeOrientation()

def apply_move(move, speed):
    """
    Applies moves to the cube state and frontend.

    Args:
        move (str): The move.
        speed (float): The turn speed.
    """

    cube.queue_move(move, speed)
    state.apply_move(orientation.translate(move))

    #print internal representation after move
    print(state.permutations)
    print(state.orientations)
    print("\n")

def scramble(n=20):
    """Scrambles the cube with 20 random moves."""

    scramble = []

    for _ in range(n):
        random_move = random.choice(representation_constants.MOVES)
        scramble.append(random_move) #save the scramble
        apply_move(random_move, interface_constants.SCRAMBLE_SPEED)

    #output the scramble
    print("scramble: ")
    print(scramble)

def input(key):
    """Ursina function to handle inputs."""

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


#guard so code only runs when main running
if __name__ == "__main__":

    #create the app and enable camera
    app = Ursina()
    EditorCamera()

    #run
    app.run()
    