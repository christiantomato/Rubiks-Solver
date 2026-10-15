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
            1 = clockwise turn from the UD face
            2 = counter clockwise turn from the UD face
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

        Since we always fix our orientation so that the UFR corner is always in the UFR location,
        moves affecting the UFR like U perform a correction rotation.

        For example, applying U while maintaining our canonical orientation is:

            U y' = y' D

        And since our states do not encode rotations like y', U = D are equivalent in the representation.

        Therefore {D, B, L} is a generator for the group. 

        Args:
            move (str): The move to apply. Must be one of:
            U, U', D, D', F, F', B, B', R, R', L, L'
        """

        match move:
            case "U" | "D":
                self._D()
            case "U'" | "D'":
                self._D_prime()
            case "F" | "B": 
                self._B()
            case "F'" | "B'": 
                self._B_prime()
            case "R" | "L":
                self._L()
            case "R'" | "L'":
                self._L_prime()
            case _:
                print("not a valid move.")

    """
    D corner cycle: DFR -> DBR -> DBL -> DFL -> DFR 
    D' corner cycle: DFR <- DBR <- DBL <- DFL <- DFR
    """

    def _D(self):
        #save the corner and its orientation for ecah location that is affected by this cycle
        dfr_c = self.permutations[self.DFR] 
        dbr_c = self.permutations[self.DBR]
        dbl_c = self.permutations[self.DBL] 
        dfl_c = self.permutations[self.DFL]
        dfr_o = self.orientations[self.DFR] 
        dbr_o = self.orientations[self.DBR] 
        dbl_o = self.orientations[self.DBL] 
        dfl_o = self.orientations[self.DFL]
        #assign them their new location (no orientation changing since we are in UD)
        self.permutations[self.DFR] = dfl_c
        self.permutations[self.DBR] = dfr_c
        self.permutations[self.DBL] = dbr_c
        self.permutations[self.DFL] = dbl_c 
        self.orientations[self.DFR] = dfl_o
        self.orientations[self.DBR] = dfr_o
        self.orientations[self.DBL] = dbr_o
        self.orientations[self.DFL] = dbl_o 
    
    def _D_prime(self):
        #save the corner and its orientation for ecah location that is affected by this cycle
        dfr_c = self.permutations[self.DFR] 
        dbr_c = self.permutations[self.DBR]
        dbl_c = self.permutations[self.DBL] 
        dfl_c = self.permutations[self.DFL]
        dfr_o = self.orientations[self.DFR] 
        dbr_o = self.orientations[self.DBR] 
        dbl_o = self.orientations[self.DBL] 
        dfl_o = self.orientations[self.DFL]
        #assign them their new location (no orientation changing since we are in UD)
        self.permutations[self.DFR] = dbr_c
        self.permutations[self.DBR] = dbl_c
        self.permutations[self.DBL] = dfl_c
        self.permutations[self.DFL] = dfr_c
        self.orientations[self.DFR] = dbr_o
        self.orientations[self.DBR] = dbl_o
        self.orientations[self.DBL] = dfl_o
        self.orientations[self.DFL] = dfr_o

    """
    L corner cycle: UFL -> DFL -> DBL -> UBL -> UFL 
    L' corner cycle: UFL <- DFL <- DBL <- UBL <- UFL
    """

    def _L(self):
        #save the corner and its orientation for each location that is affected by this cycle.
        ufl_c = self.permutations[self.UFL]
        dfl_c = self.permutations[self.DFL]
        dbl_c = self.permutations[self.DBL]
        ubl_c = self.permutations[self.UBL]
        ufl_o = self.orientations[self.UFL]
        dfl_o = self.orientations[self.DFL]
        dbl_o = self.orientations[self.DBL] 
        ubl_o = self.orientations[self.UBL]
        #assign them their new location
        self.permutations[self.UFL] = ubl_c
        self.permutations[self.DFL] = ufl_c
        self.permutations[self.DBL] = dfl_c
        self.permutations[self.UBL] = dbl_c 
        #assign them their new orientations
        self.orientations[self.UFL] = (ubl_o + 1) % 3
        self.orientations[self.DFL] = (ufl_o + 2) % 3
        self.orientations[self.DBL] = (dfl_o + 1) % 3
        self.orientations[self.UBL] = (dbl_o + 2) % 3
    
    def _L_prime(self):
        #save the corner and its orientation for each location that is affected by this cycle.
        ufl_c = self.permutations[self.UFL]
        dfl_c = self.permutations[self.DFL]
        dbl_c = self.permutations[self.DBL]
        ubl_c = self.permutations[self.UBL]
        ufl_o = self.orientations[self.UFL]
        dfl_o = self.orientations[self.DFL]
        dbl_o = self.orientations[self.DBL] 
        ubl_o = self.orientations[self.UBL]
        #assign them their new location
        self.permutations[self.UFL] = dfl_c
        self.permutations[self.DFL] = dbl_c
        self.permutations[self.DBL] = ubl_c
        self.permutations[self.UBL] = ufl_c 
        #assign them their new orientations
        self.orientations[self.UFL] = (dfl_o - 2) % 3
        self.orientations[self.DFL] = (dbl_o - 1) % 3
        self.orientations[self.DBL] = (ubl_o - 2) % 3
        self.orientations[self.UBL] = (ufl_o - 1) % 3

    """
    B corner cycle: UBR -> UBL -> DBL -> DBR -> UBR
    B' corner cycle: UBR <- UBL <- DBL <- DBR <- UBR
    """

    def _B(self):
        #save the corner and its orientation for each location that is affected by this cycle.
        ubr_c = self.permutations[self.UBR]
        ubl_c = self.permutations[self.UBL]
        dbl_c = self.permutations[self.DBL]
        dbr_c = self.permutations[self.DBR]
        ubr_o = self.orientations[self.UBR]
        ubl_o = self.orientations[self.UBL]
        dbl_o = self.orientations[self.DBL] 
        dbr_o = self.orientations[self.DBR]
        #assign them their new location
        self.permutations[self.UBR] = dbr_c
        self.permutations[self.UBL] = ubr_c 
        self.permutations[self.DBL] = ubl_c 
        self.permutations[self.DBR] = dbl_c 
        #assign them their new orientations
        self.orientations[self.UBR] = (dbr_o + 2) % 3
        self.orientations[self.UBL] = (ubr_o + 1) % 3
        self.orientations[self.DBL] = (ubl_o + 2) % 3
        self.orientations[self.DBR] = (dbl_o + 1) % 3
    
    def _B_prime(self):
        #save the corner and its orientation for each location that is affected by this cycle.
        ubr_c = self.permutations[self.UBR]
        ubl_c = self.permutations[self.UBL]
        dbl_c = self.permutations[self.DBL]
        dbr_c = self.permutations[self.DBR]
        ubr_o = self.orientations[self.UBR]
        ubl_o = self.orientations[self.UBL]
        dbl_o = self.orientations[self.DBL] 
        dbr_o = self.orientations[self.DBR]
        #assign them their new location
        self.permutations[self.UBR] = ubl_c
        self.permutations[self.UBL] = dbl_c 
        self.permutations[self.DBL] = dbr_c
        self.permutations[self.DBR] = ubr_c
        #assign them their new orientations
        self.orientations[self.UBR] = (ubl_o - 1) % 3
        self.orientations[self.UBL] = (dbl_o - 2) % 3
        self.orientations[self.DBL] = (dbr_o - 1) % 3
        self.orientations[self.DBR] = (ubr_o - 2) % 3
