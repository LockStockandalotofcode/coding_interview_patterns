from typing import List
from collections import deque

def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    # base case
    dict_set = set(dictionary)
    if start not in dict_set or end not in dict_set:
        return 0
    if start == end:
        return 1
    
    # BFS level order traversal to track shortest distance
    dist = 0
    queue = deque([start])
    visited = set([start])
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    while queue:
        for _ in range(len(queue)):
            curr_word = queue.popleft()
            # when end word is reached, return distance
            if end == curr_word:
                return dist + 1
            # recurse down to each neighbor of current word
            for i in range(len(curr_word)):
                for c in lowercase_letters:
                    new_word = curr_word[:i] + c + curr_word[i+1 : ]
                    if new_word not in visited and new_word in dict_set:
                        visited.add(new_word)
                        queue.append(new_word)
        dist += 1
         # dist increases for each level

    return 0 # if end can't be reached