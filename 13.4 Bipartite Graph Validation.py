from typing import List

def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    colors = [0] * len(graph)  # 0 means uncolored/unvisited

    def dfs(node: int, color: int, colors: List[int]) -> bool:
        colors[node] = color  # Color the current node (either 1 or -1)

        for neighbor in graph[node]:
            # If a neighbor has the same color as the current node, it's a violation!
            if colors[neighbor] == color:
                return False
            # If the neighbor hasn't been colored yet, color it with the OPPOSITE color
            if colors[neighbor] == 0 and not dfs(neighbor, -color, colors):
                return False
        return True
    
    for i in range(len(graph)):
        # If a node is uncolored, it's the start of a new graph component
        if colors[i] == 0 and not dfs(i, 1,  colors):
            return False
    return True