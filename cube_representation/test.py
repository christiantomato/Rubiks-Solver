from cube2x2 import Cube2x2

def test():
    cube = Cube2x2()

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