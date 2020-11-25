from testData import testInput

# Print unresolved matrix

# Split known numbers and unknown numbers into separate arrays
# keep track of fixed fields and unknown fields

# sudoku data
# knownArr: - input dict. (pos,value)[]
# unknownArr: full sudoku - input dict. (pos, value = 0)[]
# entire sudoku is union known + unknown

# Search
# Traverse unknown
# 0. Initiate pointer at index i = 0;
# 1. If unknownArr[i] === 9 - Set unknownArr[i] to zero. Decrement i & new iteration.
# 2. Increment unknownArr[i]. 
# 3. Check if knownArr + unknownArr are valid with current partial fill.
# 4. If valid - increment i. If i > len(unknownArr): Found solution, exit algorithm. If not valid - increment unknownArr[i]. New iteration.

# Print solved matrix
