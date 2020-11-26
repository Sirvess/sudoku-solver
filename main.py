from testData import known, unknown 
import numpy as np

# Create indeces of rows / columns / squares .
# Assuming 9x9 grid for now
# Will make it easier to validate in each iteration
rowIndeces = np.arange(81)
print(rowIndeces)
# def getRowIndeces(index):
# def getColIndeces(index):
# def getSquareIndeces(index):


# Search
# Traverse unknown
# 0. Initiate pointer at index i = 0;
# 1. If unknownArr[i] === 9 - Set unknownArr[i] to zero. Decrement i & new iteration.
# 2. Increment unknownArr[i]. 
# 3. Check if knownArr + unknownArr are valid with current partial fill.
# 4. If valid - increment i. If i > len(unknownArr): Found solution, exit algorithm. If not valid - increment unknownArr[i]. New iteration.

# Print solved matrix
