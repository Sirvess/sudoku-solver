import numpy as np
import math

from testData import difficultTest

# Helper function for 9x9 grid
def checkIfValid(unknownNode, knownGrid, unknownNodes):
    if unknownNode["val"] == 0:
        return False
    currentGrid = knownGrid + list(
        filter(
            lambda node: not (
                node["x"] == unknownNode["x"] and node["y"] == unknownNode["y"]
            ),
            unknownNodes,
        )
    )
    # Get row
    row = list(filter(lambda node: node["y"] == unknownNode["y"], currentGrid))
    rowValues = list(map(lambda node: node["val"], row))
    # Get column
    col = list(filter(lambda node: node["x"] == unknownNode["x"], currentGrid))
    colValues = list(map(lambda node: node["val"], col))
    # Get square
    square = list(
        filter(
            lambda node: (
                node["x"]
                in range(
                    (math.floor(unknownNode["x"] / 3) * 3),
                    math.floor(unknownNode["x"] / 3) * 3 + 3,
                )
            )
            and (
                node["y"]
                in range(
                    (math.floor(unknownNode["y"] / 3) * 3),
                    math.floor(unknownNode["y"] / 3) * 3 + 3,
                )
            ),
            currentGrid,
        )
    )
    squareValues = list(map(lambda node: node["val"], square))

    existingValues = rowValues + colValues + squareValues
    return unknownNode["val"] not in existingValues


def solveSudoku(known):
    # Assuming 9x9 grid for now
    GRID_SIZE = 9

    # Initialize unknowns
    # TODO would be nice to do this in cleaner way...
    unknown = []
    for j in range(0, 9):
        for i in range(0, 9):
            exists = list(
                filter(
                    lambda exists: exists,
                    list(map(lambda node: node["x"] == i and node["y"] == j, known)),
                )
            )
            if len(exists) == 0:
                unknown.append({"x": i, "y": j, "val": 0})

    # Initialize known grid
    sudokuGrid = np.zeros((GRID_SIZE, GRID_SIZE))
    for a in known:
        sudokuGrid[a["x"]][a["y"]] = a["val"]

    # Initialize pointer and solved
    i = 0
    solved = False
    iterations = 0

    # Search for correct value using backtracking algorithm
    #
    # Description of algorithm:
    # 0. Initiate pointer at index i = 0;
    # 1. If unknownArr[i] === 9 - Set unknownArr[i] to zero. Decrement i & new iteration.
    # 2. Increment unknownArr[i]
    # 3. Check if knownArr + unknownArr are valid with current partial fill.
    # 4. If valid - increment i. If i > len(unknownArr): Found solution, exit algorithm. If not valid - increment unknownArr[i]. New iteration.

    while i < len(unknown) and not solved:
        iterations += 1
        if iterations % 10000 == 0:
            print("Current iteration: ", iterations)
        if unknown[i]["val"] == 9:
            if i == 0:
                break
            unknown[i]["val"] = 0
            i = i - 1
            continue
        unknown[i]["val"] = unknown[i]["val"] + 1
        if checkIfValid(unknown[i], known, unknown):
            i += 1
            if i > len(unknown) - 1:
                solved = True
                break

    # Print results
    print("Solved?", solved)
    print("\nIterations required", iterations)
    print("\nResulting value of unknowns", unknown)


if __name__ == "__main__":
    known = difficultTest

    # Check if known values are valid;
    if False not in map(lambda node: (checkIfValid(node, [], known)), known):
        solveSudoku(known)
    else:
        print("Input not valid")
