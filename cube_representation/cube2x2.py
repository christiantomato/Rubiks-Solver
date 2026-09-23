

class Cube2x2: 
    """Represents the state of the 2x2 cube.
    
    This definition allows us to encapsulate the 2x2 as a mathematical group. 
    """

    def __init__(self):
        """Initalizes a solved 2x2 cube. 

        The convention fixes the UFR corner with white top and green front. 
        Every other corner is then given an index starting from DFR = 0, 
        clockwise along the F face, and then clockwise again on the B side. 
        Corners are also represented in a 3D coordinate system where the 
        reference corner is in the 1st of the 8 quadrants.

        DFR = 0
        DFL = 1
        UFL = 2
        UBR = 3
        DBR = 4
        DBL = 5
        UBL = 6

        The orientations are encoded as a number belonging to mod 3 where 0 represents correctly oriented.
        """

        #initalize the solve state
        self.permutations = [0, 1, 2, 3, 4, 5, 6] #each corner in its location
        self.orientations = [0, 0, 0, 0, 0, 0, 0] #each corner oriented

    def apply_move(self, move):
            """Applies a single generator move to the cube state.

            move: string identifier for the move (e.g. "U")
            """

