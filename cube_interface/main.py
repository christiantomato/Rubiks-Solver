from ursina import *

#create the app
app = Ursina()

#create a demo entity
cube = Entity(model='cube', color=color.red, scale=1)

#enable the camera
EditorCamera()

#run
app.run()