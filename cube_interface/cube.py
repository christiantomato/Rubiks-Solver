from ursina import *
from corner import Corner
from itertools import product
import constants

class Cube: 

    """
    Represents the entire 2x2 cube for the frontend, and sends cube data to the backend. 

    Attributes:
        corners (list[Corner]): each corner piece of the cube. 
    """

    def __init__(self):

        """Creates the 8 corner pieces."""

        self.turning = False #flag for turning animations
        self.corners = [] #init the empty list of corners

        #iterate over the 8 possible coordinate positions (x, y, z) where each coordinate belongs to {-0.5, 0.5}
        for coordinates in product((0.5, -0.5), repeat=3):
            corner_entity = Entity(position=coordinates, model='cube', color=color.black, scale=1)
            sticker_entities = []

            #loop through the axes to assign stickers for the cubie
            for axis in range(3):
                #get sign
                sign = 1 if coordinates[axis] > 0 else -1 

                #build position vector by assigning coordinate slightly in front of cube face
                sticker_pos = Vec3(0, 0, 0) 
                sticker_pos[axis] = sign * 0.51

                #get the rotation
                sticker_rot = constants.rotation[(axis, sign)]
                #get color 
                sticker_col = constants.colors[(axis, sign)]

                #build the entity 
                sticker = Entity(parent=corner_entity, position=sticker_pos, rotation=sticker_rot, model="quad", color=sticker_col, scale=0.9)

            #add the built corner
            self.corners.append(
                Corner(corner_entity, sticker_entities, coordinates, constants.corner_indices[coordinates])
            )

    def _turn(self, axis, sign, angle): 

        """Turns the 4 selected corners of the cube."""

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
        pivot.animate(attr, angle, duration=0.5, curve=curve.in_out_quad)

        # call _finish_turn once the animation is done
        invoke(self._finish_turn, selected, pivot, delay=0.5)

    def _finish_turn(self, selected, pivot): 
        #detach and round for float inaccuracies
        for c in selected:
            c.entity.world_parent = scene
            c.position = tuple(round(v * 2) / 2 for v in c.entity.world_position)
            c.entity.rotation = tuple(round(r / 90) * 90 for r in c.entity.world_rotation)
            c.entity.position = c.position
        destroy(pivot)
        self.turning = False

    """
    Every type of turn.
    """

    def U(self): 
        self._turn(1, 1, 90)

    def U_prime(self):
        self._turn(1, 1, -90) 

    def D(self): 
        self._turn(1, -1, -90)

    def D_prime(self): 
        self._turn(1, -1, 90)

    def F(self): 
        self._turn(2, -1, 90)

    def F_prime(self):
        self._turn(2, -1, -90) 

    def B(self): 
        self._turn(2, 1, -90)

    def B_prime(self): 
        self._turn(2, 1, 90)

    def R(self): 
        self._turn(0, 1, 90)

    def R_prime(self):
        self._turn(0, 1, -90) 

    def L(self): 
        self._turn(0, -1, -90)

    def L_prime(self): 
        self._turn(0, -1, 90)
