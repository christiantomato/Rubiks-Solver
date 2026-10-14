#new update broke audio (not that we need)
from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from ursina import *
from cube import Cube

#create the app
app = Ursina()

#create a cube
my_cube = Cube()

#keyboard inputs
def input(key):
    is_prime = held_keys['shift']

    if key == 'r':
        my_cube.R() if not is_prime else my_cube.R_prime()
    elif key == 'l':
        my_cube.L() if not is_prime else my_cube.L_prime()
    elif key == 'u':
        my_cube.U() if not is_prime else my_cube.U_prime()
    elif key == 'd':
        my_cube.D() if not is_prime else my_cube.D_prime()
    elif key == 'f':
        my_cube.F() if not is_prime else my_cube.F_prime()
    elif key == 'b':
        my_cube.B() if not is_prime else my_cube.B_prime()

#enable the camera
EditorCamera()

#run
app.run()