from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    res = []
    # define boundaries of matrix
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= bottom:
        # move left to right, top row, then change top boundary
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1

        # move top to bottom, rightmost(right boundary) column, then change right boundary
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # move right to left, bottom row, then change bottom boundary
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # move bottom to top, leftmost row, then change left boundary
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    
    return res