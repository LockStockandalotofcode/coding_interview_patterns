from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    first_col_zero = False
    first_row_zero = False
    # using first row and column as flag 
    # first setting flag for first row and col, before moving onto submatrix[2:][2:] if thinking of 1-based indexing

    # FIRST ROW
    for c in range(n_cols):
        if matrix[0][c] == 0:
            first_row_zero = True
            break

    # FIRST COLUMN
    for r in range(n_rows):
        if matrix[r][0] == 0:
            first_col_zero = True
            break
        
    # setting markers in first row and col for rest submatrix
    for r in range(1, n_rows):
        for c in range(1, n_cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # setting all zeroes in submatrix # traverse cell wise simpler
    for r in range(1, n_rows):
        for c in range(1, n_cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
            
    # for first row and first column
    if first_row_zero:
        for c in range(n_cols):
            matrix[0][c] = 0
        
    if first_col_zero:
        for r in range(n_rows):
            matrix[r][0] = 0