map_file = open('day3-input.txt', 'r')
tree_map = list(map(lambda x: x.strip(), map_file.readlines()))

def countTrees(ySlope, xSlope):
    posY = 0
    posX = 0
    count = 0
    while posY < len(tree_map):
        if tree_map[posY][posX] == '#':
            count += 1
        posX = (posX + xSlope) % len(tree_map[0])
        posY += ySlope
    return count

print(countTrees(1, 3))

test_slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

def multipleSlopes(slopes):
    product = 1
    for slope in slopes:
        product *= countTrees(slope[0], slope[1])
    return product

print(multipleSlopes(test_slopes))
