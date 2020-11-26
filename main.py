from testData import known, unknown 
import numpy as np

# Assuming 9x9 grid for now
GRID_SIZE = 9

# Initialize known grid
sudokuGrid = np.zeros((GRID_SIZE,GRID_SIZE))
for a in known:
    sudokuGrid[a["x"]-1][a["y"]-1] = a["val"]
    
# Search
# Traverse unknown
# 0. Initiate pointer at index i = 0;
# 1. If unknownArr[i] === 9 - Set unknownArr[i] to zero. Decrement i & new iteration.
# 2. Increment unknownArr[i]. 
# 3. Check if knownArr + unknownArr are valid with current partial fill.
# 4. If valid - increment i. If i > len(unknownArr): Found solution, exit algorithm. If not valid - increment unknownArr[i]. New iteration.

# Print solved matrix
