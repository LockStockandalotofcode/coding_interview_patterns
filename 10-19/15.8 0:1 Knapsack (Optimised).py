from typing import List

def knapsack(k: int, weights: List[int], values: List[int]) -> int:
    # 2D Space optimization

    # similar to Bottom Up DP approach but 2D
    # 2D DP table approach : items in rows, curr_capacity in columns
    # each cell records max value at curr_capacity = column value, and considering including all items starting from this index
    
    if not weights or not values or k == 0:
        return 0
    
    n_items = len(values)
    # Base case for DP table : 0 Matrix
    prev_row = [0 for _ in range(k + 1)]

    # cell traversal: starting at n item row, with curr_capacity = 1
    for start_item in range(n_items - 1, -1, -1): # row traversal
        curr_row = [0] * (k + 1)
        for curr_capacity in range(1, k+1): # column traversal, incrementing capacity
            # deteremining max value at a cell is decided by its inclusion or exclusion, if at all its allowed(less curr_capacity than allowed curr_capacity for this column)
            if weights[start_item] <= curr_capacity:
                curr_row[curr_capacity] = max(values[start_item] + prev_row[curr_capacity - weights[start_item]], prev_row[curr_capacity])
            else:
                curr_row[curr_capacity] = prev_row[curr_capacity]
        prev_row = curr_row
    
    return prev_row[k]