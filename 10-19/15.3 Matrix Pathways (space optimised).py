def matrix_pathways(m: int, n: int) -> int:
    prev_row = [1] * n

    # cell wise traversal, keeping track of current row and pre row
    for r in range(1, m):
        curr_row = [1] * n
        for c in range(1, n):
            # calculate value of cell from recursive relation
            curr_row[c] = prev_row[c] + curr_row[c-1]
        # updating the prev row only, curr_row starts with [1]*n, for each next calculation
        prev_row = curr_row
    
    return prev_row[n-1]