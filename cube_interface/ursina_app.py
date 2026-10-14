#new update broke audio (not that we need)
from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from ursina import *
from cube import Cube

#create the app
app = Ursina()

#create a cube
my_cube = Cube()

#enable the camera
EditorCamera()

#run
app.run()