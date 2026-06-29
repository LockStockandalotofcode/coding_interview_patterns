from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # 1 hashset for each row, column, subgrid
    # row and columns are mapped by index as arrays
    # subgrids are mapped as matrix, list of lists, r // 3 and c // 3 gives indices of subgrid

    if not board or not board[0] or len(board) != 9 or len(board[0]) != 9:
        return False
    
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
        
    # cell wise traversal
    for r in range(9):
        for c in range(9):
            element = board[r][c]
            # skip 0, empty cells
            if element == 0:
                continue

            if (element in row_sets[r] or element in col_sets[c] or element in subgrid_sets[r // 3][c // 3]):
                return False

            row_sets[r].add(element)
            col_sets[c].add(element)
            subgrid_sets[r // 3][c // 3].add(element)
        
    return True