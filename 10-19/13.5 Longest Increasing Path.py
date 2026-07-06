from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    res = 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]

    # helper to dfs_helper
    def is_within_bounds(r: int, c: int) -> bool:
        return (0 <= r < m) and (0 <= c < n)
    
    # dfs_helper
    def longest_path_one_cell(r: int, c: int):
        if memo[r][c] != 0:
            return memo[r][c]
        longest_path = 1 # for including the current node
        # setting up neighbors for dfs recursive traversal
        dirs = [[0,1], [-1,0], [0,-1], [1,0]]
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            if is_within_bounds(next_r, next_c) and matrix[next_r][next_c] > matrix[r][c]:
                longest_path = max(longest_path, 1 + longest_path_one_cell(next_r, next_c))

        memo[r][c] = longest_path
        return longest_path
    
    # now calculating longest path starting from  each cell of matrix, res is longest of them
    for i in range(m):
        for j in range(n):
            res = max(res, longest_path_one_cell(i,j))
    
    return res