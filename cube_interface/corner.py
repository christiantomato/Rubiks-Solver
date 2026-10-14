class Corner: 

    """
    Represents a corner piece of the cube.

    Attributes:
        corner_entity (Entity): the ursina entity of the corner.
        sticker_entities (list[Entity]): the list of sticker entities, indexed by the axis they are facing. 
        position (list[int]): specifies the coordinates of the corner piece (x, y, z), each either {0.5, -0.5}.
        corner_index (int): corresponds to which piece this corner actually is in the backend (DFR, DFL, etc.)
    """

    def __init__(self, entity, sticker_entities, position, corner_index):
        #assign attributes
        self.entity = entity 
        self.sticker_entities = sticker_entities
        self.position = position 
        self.corner_index = corner_index
