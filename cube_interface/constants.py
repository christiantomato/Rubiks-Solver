from ursina.color import rgb

"""
Ursina Camera Coordinate System:

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

Corner Indices (UFR ignored, denoted by -1): 

DFR = 0
DFL = 1
UFL = 2
UBR = 3
DBR = 4
DBL = 5
UBL = 6
"""

#rotation dictionary (based on the axis and sign)
ROTATION = {(0, 1): (0, -90, 0),
          (0, -1): (0, 90, 0),
          (1, 1): (90, 0, 0),
          (1, -1): (-90, 0, 0), 
          (2, 1): (0, 180, 0), 
          (2, -1): (0, 0, 0)
        }

#LIAHS COLORS:
#COLORS = {(0, 1): rgb(250, 102, 120),
#          (0, -1): rgb(250, 145, 65),
#          (1, 1): rgb(252, 250, 250),
#          (1, -1): rgb(252, 244, 151), 
#          (2, 1): rgb(159, 237, 252), 
#          (2, -1): rgb(148, 247, 157)
#          }

#colors dictionary (also based on axis and sign)

COLORS = {(0, 1): rgb(250, 102, 120),
          (0, -1): rgb(250, 145, 65),
          (1, 1): rgb(230, 230, 230),
          (1, -1): rgb(252, 244, 151), 
          (2, 1): rgb(159, 237, 252), 
          (2, -1): rgb(148, 247, 157)
          }

#corner index dictionary (based on position)
CORNER_INDICES = {(0.5, -0.5, -0.5): 0,
                (-0.5, -0.5, -0.5): 1,
                (-0.5, 0.5, -0.5): 2,
                (0.5, 0.5, 0.5): 3, 
                (0.5, -0.5, 0.5): 4,
                (-0.5, -0.5, 0.5): 5, 
                (-0.5, 0.5, 0.5): 6,
                (0.5, 0.5, -0.5): -1
                }

#constants for inputs
KEYS = {"u": "U", "d": "D", "f": "F", "b": "B", "r": "R", "l": "L"}
NORMAL_SPEED = 0.4
SCRAMBLE_SPEED = 0.2
