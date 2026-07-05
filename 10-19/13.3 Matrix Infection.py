from typing import List
from collections import deque

def matrix_infection(matrix: List[List[int]]) -> int:
    ones = time = 0
    queue = deque()

    # Count number of 1's uninfected cells, and append all infected cells to queue to begin with
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                ones += 1
            if matrix[i][j] == 2:
                queue.append((i, j))
    
    def is_within_bounds(r: int, c: int) -> bool:
        return (0 <= r < len(matrix)) and (0 <= c < len(matrix[0]))

    # level order traversal
    while queue and ones > 0:
        time += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            dirs = [[0,1], [1,0], [-1,0], [0,-1]]
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if is_within_bounds(next_r, next_c) and matrix[next_r][next_c] == 1:
                    ones -= 1
                    matrix[next_r][next_c] = 2
                    queue.append((next_r,next_c))
    
    return time if ones == 0 else -1
