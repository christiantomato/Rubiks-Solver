from ursina import Entity, Vec3, color
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

        self.corners = []

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
