class MergingCommunities:
    def __init__(self, n: int):
        self.uf = UnionFind(n)

    def connect(self, x: int, y: int) -> None:
        self.uf.union(x, y)

    def get_community_size(self, x: int) -> int:
        return self.uf.get_size(x)
    
class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def union(self, num1: int, num2: int) -> None:
        rep_1, rep_2 = self.find(num1), self.find(num2)
        if rep_1 != rep_2:
            if self.size[rep_1] >= self.size[rep_2]:
                self.parent[rep_2] = rep_1
                self.size[rep_1] += self.size[rep_2]
            else:
                self.parent[rep_1] = rep_2
                self.size[rep_2] += self.size[rep_1]

    def find(self, x) -> int:
        if x == self.parent[x]: # root node - parent is itself
            return x
        # path compression, helps in flattening graph
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]