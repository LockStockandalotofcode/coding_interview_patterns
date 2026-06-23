from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    # USING HASH SETS FOR CONSTANT TIME LOOKUP

    zero_rows = set()
    zero_cols = set()

    # feed data into above has sets
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    # manipulate matrix accordingly
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if c in zero_cols or r in zero_rows:
                matrix[r][c] = 0
