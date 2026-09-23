

class Cube2x2: 
    """Represents the state of the 2x2 cube.
    
    This definition allows us to encapsulate the 2x2 as a mathematical group. 
    """

    def __init__(self):
        """Initalizes a solved 2x2 cube. 

        The convention fixes the UFR corner with white top and green front. The corners are given an index
        starting there from 0, clockwise along the F face, and then clockwise again on the B side. Corners are 
        also represented in a 3D coordinate system where the reference corner is in the 1st of the 8 quadrants.

        UFR = 0
        DFR = 1
        DFL = 2
        UFL = 3
        UBR = 4
        DBR = 5
        DBL = 6
        UBL = 7

        The orientations are encoded as a number belonging to mod 3 where 0 represents correctly oriented.
        """

        self.permutations = [1, 2, 3, 4, 5, 6, 7]
        self.orientations = [0, 0, 0, 0, 0, 0, 0]
