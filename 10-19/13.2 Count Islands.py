from typing import List

def count_islands(matrix: List[List[int]]) -> int:
    # recursive solution DFS
    if not matrix or not matrix[0]:
        return 0
    visited = set()
    count = 0

    def is_within_bounds(r: int, c: int) -> bool:
        return (0 <= r < len(matrix)) and (0 <= c < len(matrix[0]))

    def single_island_helper(r: int, c: int) -> None:
        # mark cell as visited
        visited.add((r, c))
        # recurse down on any land piece that is neighbor and unvisited
        dirs = [[-1,0], [0, 1], [1, 0], [0, -1]]
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            if (is_within_bounds(next_r, next_c) and matrix[next_r][next_c] == 1 and (next_r, next_c) not in visited):
                single_island_helper(next_r, next_c)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i, j) not in visited:
                single_island_helper(i, j)
                count += 1
    return count 
