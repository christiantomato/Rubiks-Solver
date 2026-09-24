class Cube2x2:

    """Represents the state of the 2x2 cube.

    This definition captures every canonical state of the 2x2 cube.

    The convention used fixes the UFR corner with white top and green front.

    Every other corner is then given an index starting from DFR = 0,
    clockwise along the F face, and then clockwise again on the B side.

    By locking a corner in place, we eliminate redundant cases which only
    differ by a cube rotation.

    Attributes:
        permutations (list[int]): Maps each corner location to the corner
            piece currently occupying it. The indices correspond to the
            corner locations defined by the class constants.
        orientations (list[int]): Stores the orientation of each corner
            piece. Each value is in {0, 1, 2}. To assign a value, consider
            the UD sticker (white/yellow) as a reference. Then:
            0 = oriented (white/yellow on UD face)
            1 = clockwise turn from UD face
            2 = counter clockwise turn from UD face
    """

    #corner piece indices
    DFR = 0
    DFL = 1
    UFL = 2
    UBR = 3
    DBR = 4
    DBL = 5
    UBL = 6

    def __init__(self):

        """Initializes a solved 2x2 cube."""

        #initalize the solved state
        self.permutations = [self.DFR, self.DFL, self.UFL, self.UBR, self.DBR, self.DBL, self.UBL]
        self.orientations = [0, 0, 0, 0, 0, 0, 0]

    def apply_move(self, move):
        """Applies a move to the cube. 

        Args:
            move (str): The move to apply. Must be one of:
            U, U', D, D', R, R', L, L', F, F', B, B'
        """

        match move:
            case "U":
                pass

    def _U(self):
        self.D()

    def _U_prime(self):
        pass

    def _D(self):
        pass
    
    def _D_prime(self):
        pass

    def _R(self):
        pass

    def _R_prime(self):
        pass

    def _L(self):
        pass
    
    def _L_prime(self):
        pass

    def _F(self):
        pass

    def _F_prime(self):
        pass

    def _B(self):
        pass
    
    def _B_prime(self):
        pass
