# Searching for elements in 2-D matrix
# using binary search method 
# Time Comlexity: O(log(m*n)) 
# Space Complexity: O(1)

# Search function for the matrix
def searchMatrix(matrix, target):
    # base case
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = left + (right-left)/2
        mid_val = matrix[mid // cols][mid % cols]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False