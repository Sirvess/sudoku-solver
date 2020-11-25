from testData import testInput

# Print unresolved matrix

# Split known numbers and unknown numbers into separate arrays
# keep track of fixed fields and unknown fields

# sudoku data
# known: - input dict. (pos,value)[]
# unknown: full sudoku - input dict. (pos, value = 0)[]
# entire sudoku is union known + unknown

# Search
# Algorithm:
# For all unknown
# 1. Suggest 1
# 2. Check if valid
# 3. If valid - go to next
# 4. If not valid - go back to previous unknown.
# 5. If previous unknown is already 9 - go to previous unknown. If on last unknown and already at 9 - No solution.
# 6. Increment previous unknown with 1.
# 7. Repeat until on last unknown and is valid.

# Print solved matrix
