from ursina import *
from itertools import product

#create the app
app = Ursina()

"""
Coordinate System:

x: Right to Left
y: Up to Down 
z: Front to Back

They are enumerated 0, 1, 2. 
Positive/Negative signs are denoted by 1 or -1. 

ursina's camera defaults to facing (x, y, -z) so our cube faces will be
+x / (0, 1): R (red)
-x / (0, -1): L (orange)
+y / (1, 1): U (white) 
-y / (1, -1): D (yellow)
+z / (2, 1): B (blue)
-z / (2, -1): F (green)
"""

#rotation dictionary (based on the axis and sign)
rotation = {(0, 1): (0, -90, 0),
          (0, -1): (0, 90, 0),
          (1, 1): (90, 0, 0),
          (1, -1): (-90, 0, 0), 
          (2, 1): (0, 180, 0), 
          (2, -1): (0, 0, 0)
        }

#colors dictionary (also based on axis and sign)
colors = {(0, 1): color.pink,
          (0, -1): color.orange,
          (1, 1): color.white,
          (1, -1): color.yellow, 
          (2, 1): color.blue, 
          (2, -1): color.green
          }

#create the 8 corners

#iterate over the 8 possible coordinate positions (x, y, z) where each coordinate belongs to {-0.5, 0.5}
for coordinates in product((0.5, -0.5), repeat=3):
    cubie = Entity(position=coordinates, model='cube', color=color.black, scale=1)

    #loop through the axes to assign stickers for the cubie
    for axis in range(3):
        #get sign
        sign = 1 if coordinates[axis] > 0 else -1 

        #build position vector by assigning coordinate slightly in front of cube face
        sticker_pos = Vec3(0, 0, 0) 
        sticker_pos[axis] = sign * 0.51

        #get the rotation
        sticker_rot = rotation[(axis, sign)]
        #get color 
        sticker_col = colors[(axis, sign)]

        #build the entity 
        sticker = Entity(parent=cubie, position=sticker_pos, rotation=sticker_rot, model="quad", color=sticker_col, scale=0.9)

#enable the camera
EditorCamera()

#run
app.run()