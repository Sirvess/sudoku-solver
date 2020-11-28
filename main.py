from testData import known, unknown 
import numpy as np
import math

# Assuming 9x9 grid for now
GRID_SIZE = 9

# Initialize known grid
sudokuGrid = np.zeros((GRID_SIZE,GRID_SIZE))
for a in known:
    sudokuGrid[a["x"]][a["y"]] = a["val"]

def checkIfValid(unknownNode, knownGrid,unknownNodes):
    currentGrid = knownGrid + list(filter(lambda node: node["x"] != unknownNode["x"] & node["y"] != unknownNode["y"],unknownNodes))
    # Get row
    row = list(filter(lambda node: node["y"] == unknownNode["y"],currentGrid))
    rowValues = list(map(lambda node: node["val"],row))
    # Get column
    col = list(filter(lambda node: node["x"] == unknownNode["x"],currentGrid))
    colValues = list(map(lambda node: node["val"],col))
    # Get square
    square = list(filter(lambda node: (node["x"] in range((math.floor(unknownNode["x"] / 3) * 3), math.floor(unknownNode["x"] / 3) * 3 + 3 )) &
                                  (node["y"] in range((math.floor(unknownNode["y"] / 3) * 3), math.floor(unknownNode["y"] / 3) * 3 + 3 ))
                                  , currentGrid))
    squareValues = list(map(lambda node: node["val"],square))

    existingValues = rowValues + colValues + squareValues
    return unknownNode["val"] not in existingValues

# Initialize pointer and solved
i = 0
solved = False;

while(i < len(unknown) & ~solved):
    if(unknown[i]["val"] == 9):
        if(i == 0):
            break;
        unknown[i]["val"] = 0;
        i = i - 1;
        continue;
    unknown[i]["val"] = unknown[i]["val"] + 1
    # Should probably send in current node, entire unknown arr, and entire sudokugrid
    # print(unknown[i],known,unknown)
    if(checkIfValid(unknown[i], known,unknown)):
        i +=1
        if(i > len(unknown)-1):
            solved = True
            break;

print("Solved?",solved)
print("Resulting value of unknowns",unknown)
# Search
# Traverse unknown
# 0. Initiate pointer at index i = 0;
# 1. If unknownArr[i] === 9 - Set unknownArr[i] to zero. Decrement i & new iteration.
# 2. Increment unknownArr[i]. 
# 3. Check if knownArr + unknownArr are valid with current partial fill.
# 4. If valid - increment i. If i > len(unknownArr): Found solution, exit algorithm. If not valid - increment unknownArr[i]. New iteration.

