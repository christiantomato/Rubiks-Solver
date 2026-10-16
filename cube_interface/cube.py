from ursina import *
from itertools import product
from collections import deque
from cube_interface import constants
from cube_interface.corner import Corner


class Cube: 

    """
    Represents the entire 2x2 cube for the frontend, and sends cube data to the backend. 

    Attributes:
        corners (list[Corner]): each corner piece of the cube. 
    """

    def __init__(self):
        """Creates the 8 corner pieces and initalizes move queue."""

        self.corners = [] #init the empty list of corners
        self.move_queue = deque() #move queue
        self.turning = False #flag for turning animations


        #iterate over the 8 possible coordinate positions (x, y, z) where each coordinate belongs to {-0.5, 0.5}
        for coordinates in product((0.5, -0.5), repeat=3):
            corner_entity = Entity(position=coordinates, model='cube', color=color.white, scale=1)
            sticker_entities = []

            #loop through the axes to assign stickers for the cubie
            for axis in range(3):
                #get sign
                sign = 1 if coordinates[axis] > 0 else -1 

                #build position vector by assigning coordinate slightly in front of cube face
                sticker_pos = Vec3(0, 0, 0) 
                sticker_pos[axis] = sign * 0.51

                #get the rotation
                sticker_rot = constants.ROTATION[(axis, sign)]
                #get color 
                sticker_col = constants.COLORS[(axis, sign)]

                #build the entity 
                sticker = Entity(parent=corner_entity, position=sticker_pos, rotation=sticker_rot, model="quad", color=sticker_col, scale=0.9)

            #add the built corner
            self.corners.append(
                Corner(corner_entity, sticker_entities, coordinates, constants.CORNER_INDICES[coordinates])
            )

    def queue_move(self, move, turn_speed): 
        """Queues a move to be done on the cube since it needs to be animated, then plays next move in queue.

        Args: 
            move (str): The move to queue.
            turn_speed (float): Speed of the animation.
        """
        
        self.move_queue.append((move, turn_speed))
        self._play_next()

    def _play_next(self):
        """Deques the next move if nothing is turning and there is still a move."""

        if self.turning or not self.move_queue:
            return 
        
        move, speed = self.move_queue.popleft()
        self._apply_move(move, speed)

    def _apply_move(self, move, turn_speed):
            """
            Applies a move to the frontend cube.
    
            Args:
                move (str): The move to apply. Must be one of:
                {U, U', D, D', F, F', B, B', R, R', L, L'}
                turn_speed (int): Speed of the animation.
            """
    
            match move:
                case "U":
                    self._U(turn_speed)
                case "U'":
                    self._U_prime(turn_speed)
                case "D":
                    self._D(turn_speed)
                case "D'":
                    self._D_prime(turn_speed)
                case "F":
                    self._F(turn_speed)
                case "F'":
                    self._F_prime(turn_speed)
                case "B":
                    self._B(turn_speed)
                case "B'":
                    self._B_prime(turn_speed)
                case "R":
                    self._R(turn_speed)
                case "R'":
                    self._R_prime(turn_speed)
                case "L":
                    self._L(turn_speed)
                case "L'":
                    self._L_prime(turn_speed)
                case _:
                    print("not a valid move.")

    def _turn(self, axis, sign, angle, duration): 
            """
            Turns the 4 selected corners of the cube.
            
            Args:
                axis (int): The axis we are turning about.
                sign (int): Either the positive or negative side of the axis.
                angle (int): 90 or -90 degrees based on the direction of the turn. 
                duration (float): The duration of the turn animation. 
            """
    
            if self.turning: 
                return 
            else: self.turning = True
    
            #select the corners on the face 
            selected = [c for c in self.corners if c.position[axis] * sign > 0]
    
            #group them under a pivot at the origin
            pivot = Entity() 
            for c in selected: 
                c.entity.world_parent = pivot
    
            #determine the rotation type based on axis and animate the rotation
            attr = ('rotation_x', 'rotation_y', 'rotation_z')[axis]
            pivot.animate(attr, angle, duration, curve=curve.in_out_quad)
    
            # call _finish_turn once the animation is done, give some buffer time
            invoke(self._finish_turn, selected, pivot, delay=duration + 0.05)
    
    def _finish_turn(self, selected, pivot): 
        """
        Concludes a turn.
        
        Args: 
            selected (list(Corner)): The corners which were affected by the turn. 
            pivot (Entity): The temp entity at the origin which we rotated about. 
        """

        #detach and round for float inaccuracies
        for c in selected:
            c.entity.world_parent = scene
            c.position = tuple(round(v * 2) / 2 for v in c.entity.world_position)
            c.entity.rotation = tuple(round(r / 90) * 90 for r in c.entity.world_rotation)
            c.entity.position = c.position
        destroy(pivot)
        self.turning = False

        #play next
        self._play_next()

    """
    Every type of turn.
    """

    def _U(self, speed): 
        self._turn(1, 1, 90, speed)

    def _U_prime(self, speed):
        self._turn(1, 1, -90, speed) 

    def _D(self, speed): 
        self._turn(1, -1, -90, speed)

    def _D_prime(self, speed): 
        self._turn(1, -1, 90, speed)

    def _F(self, speed): 
        self._turn(2, -1, 90, speed)

    def _F_prime(self, speed):
        self._turn(2, -1, -90, speed) 

    def _B(self, speed): 
        self._turn(2, 1, -90, speed)

    def _B_prime(self, speed): 
        self._turn(2, 1, 90, speed)

    def _R(self, speed): 
        self._turn(0, 1, 90, speed)

    def _R_prime(self, speed):
        self._turn(0, 1, -90, speed) 

    def _L(self, speed): 
        self._turn(0, -1, -90, speed)

    def _L_prime(self, speed): 
        self._turn(0, -1, 90, speed)
