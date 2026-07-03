from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_all_words_on_a_board(board: List[List[str]], words: List[str]) -> List[str]:
    # make a trie of input words, with word attribute
    root = TrieNode()
    

    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    
    res = [] # store final result

    # call dfs from each board cell that is root node's children
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in root.children:
                char = board[r][c]
                dfs(board, r, c, root.children[char], res)
    
    return res

    
def dfs(board: List[List[str]], r: int, c: int, node: TrieNode, res: List[str]) -> None:
    # check final condition
    # search for next char of word in adjacent cells, recursively search adjacent cells, marking current cell as visited,
    # backtracking whenever next character not found

    if node.word: # node.word attribute not null meaning end of word
        res.append(node.word)
        # edge case handling: to avoid counting same word again (in case of duplicates on board), mark its word attribute
        node.word = None
    
    temp = board[r][c]
    board[r][c] = '#'
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if is_within_bounds(next_r, next_c, board) and board[next_r][next_c] in node.children:
            char = board[next_r][next_c]
            dfs(board, next_r, next_c, node.children[char], res)
    board[r][c] = temp

def is_within_bounds(r: int, c: int, board: List[str]) -> bool:
    return 0 <= r < len(board) and 0 <= c < len(board[0])