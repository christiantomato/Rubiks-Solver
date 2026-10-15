"""
Mapping Orientation Changes Between State and Frontend Cube: 

Since UFR moves affect our fixed corner, when applied to the front end cube the backend representation
will treat it as a DBL move with a rotation. Hence, we have to fix the disparity between the orientations of 
the 2 representations (Ex. after an R move, a U move is no longer a U move on the state, rather an F move).

This is a bijective mapping from frontend frame -> state frame. 
"""

U_MAP = {'R': 'B', 
         'L': 'F', 
         'U': 'U', 
         'D': 'D', 
         'B': 'L', 
         'F': 'R'}

U_INV_MAP = {'R': 'F', 
             'L': 'B', 
             'U': 'U', 
             'D': 'D', 
             'B': 'R', 
             'F': 'L'}

F_MAP = {'R': 'U', 
         'L': 'D', 
         'U': 'L', 
         'D': 'R', 
         'B': 'B', 
         'F': 'F'}

F_INV_MAP = {'R': 'D', 
             'L': 'U', 
             'U': 'R', 
             'D': 'L', 
             'B': 'B', 
             'F': 'F'}

R_MAP = {'R': 'R', 
         'L': 'L', 
         'U': 'F', 
         'D': 'B', 
         'B': 'U', 
         'F': 'D'}

R_INV_MAP = {'R': 'R', 
             'L': 'L', 
             'U': 'B', 
             'D': 'F', 
             'B': 'D', 
             'F': 'U'}

#valid moves that can be made
MOVES = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]
