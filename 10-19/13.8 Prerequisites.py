from typing import List
from collections import defaultdict, deque

def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
    # make graph : adj list
    # record in-degrees as well
    graph = defaultdict(list)
    indegrees = [0] * n
    for prereq, course in prerequisites:
        graph[prereq].append(course)
        indegrees[course] += 1
    
    # populate queue with 0-indegree courses, to perofrm topological sources
    # queue only stores 0-indegree courses ever, so if cycle exists, these courses are never added to queue in the first place, so the return statement is always processed, and queue can remain empty even when all courses haven't been processed through queue, so it doesn't make an infinite loop when there is a cycle
    queue = deque()
    enrolled_courses = 0
    # populate queue with 0-indegree courses
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()
        enrolled_courses += 1
        for neighbor in graph[course]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    return enrolled_courses == n