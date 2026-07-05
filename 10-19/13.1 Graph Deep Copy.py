from ds import GraphNode

"""
Definition of GraphNode:
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
"""

def graph_deep_copy(node: GraphNode) -> GraphNode:
    if not node:
        return None
    
    return dfs_helper(node)

def dfs_helper(node: GraphNode, cloned_map = {}) -> GraphNode:
    if node in cloned_map:
        return cloned_map[node]
    # create clone
    cloned_node = GraphNode(node.val)
    # add to cloned_map hashmap for nodes that have been cloned, og node -> cloned node
    cloned_map[node] = cloned_node
    # recurse for all neighbors
    for neighbor in node.neighbors:
        cloned_neighbor = dfs_helper(neighbor)
        cloned_node.neighbors.append(cloned_neighbor)
    return cloned_node