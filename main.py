from ursina import *

#create the app
app = Ursina()

#create a demo entity
cube = Entity(model='cube', color=color.pink, scale=1)

#enable the camera
EditorCamera()

#run
app.run()