from testData import testInput

# Print unresolved matrix
# Format array into "sudoku" form
# print("\nUnsolved sudoku:")
# for i in testInput:
#     print(i)

# Initialize backlog
backlog = matrix[0];

# Search
# Algorithm:
# For empty cells
# 1. Suggest 1
# 2. Check if valid
# 3. If valid - go to next
# 4. If not valid - go back to previous unknown.
# 5. If previous unknown is already 9 - go to previous unknown. If on last unknown and already at 9 - No solution.
# 6. Increment previous unknown with 1.
# 7. Repeat

# Print solved matrix
