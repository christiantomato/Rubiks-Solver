from cube_representation.cube_state import CubeState

def test():
    cube = CubeState()

    cube.apply_move("R")
    cube.apply_move("U")
    cube.apply_move("D")

    print(cube.permutations)
    print(cube.orientations)

    cube.apply_move("D'")
    cube.apply_move("U'")
    cube.apply_move("R'")

    print(cube.permutations)
    print(cube.orientations)

test()