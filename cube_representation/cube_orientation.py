from cube_representation import constants

class CubeOrientation:
    """Tracks how the state's frame is rotated relative to the frontend's.

    Attributes:
        mapping (dict[str, str]): frontend face -> state face
    """

    def __init__(self):
        """Starts with the identity mapping."""
        self.mapping = {'R': 'R', 'L': 'L', 'U': 'U', 'D': 'D', 'B': 'B', 'F': 'F'}

    def translate(self, move):
        """
        Converts a frontend move into the matching state move.

        The face is looked up in the mapping, a prime carries over unchanged.

        Args:
            move (str): A frontend move, e.g. "R" or "R'".

        Returns:
            str: The move as the state should see it.
        """

        #get the face the move turns
        face = move[0]
        #watch for if prime
        prime = move[1:]
        #put through the map, append prime if needed
        translated_move = self.mapping[face] + prime

        #update the mapping and return move 
        self._update(translated_move)
        return translated_move

    def _update(self, translated_move):
        """
        Updates the mapping after a move is applied to the state.

        Only UFR moves touching the fixed corner cause a hidden rotation. 
        DBL moves leave the mapping unchanged.

        Args:
            translated_move (str): The move as the state saw it.
        """

        #check if the move actually changes the cube orientation
        face = translated_move[0]
        if face == 'D' or face == 'B' or face == 'L': return

        #otherwise, compose the mapping
        match translated_move: 
            case "U": 
                self._compose(constants.U_map)
            case "U'":
                self._compose(constants.U_inv_map)
            case "F": 
                self._compose(constants.F_map)
            case "F'":
                self._compose(constants.F_inv_map)
            case "R": 
                self._compose(constants.R_map)
            case "R'": 
                self._compose(constants.R_inv_map)
            case _: 
                print("not a valid move.")

    def _compose(self, rotation):
        """
        Applies a rotation map to every value in the current mapping.

        Args: 
            rotation (dict): The specified rotation map. 
        """
        self.mapping = {f: rotation[s] for f, s in self.mapping.items()}
