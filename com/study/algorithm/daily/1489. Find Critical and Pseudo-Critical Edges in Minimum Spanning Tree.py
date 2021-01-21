
class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.numComponent = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    #Two point merge
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False
        else:
            self.parent[parent_y] = parent_x
            self.numComponent -= 1
            return True

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]] [边的索引号]
        """
        uf = UnionFind(n)
        for i, edge in enumerate(edges):
            edge.append(i)

        edges = sorted(edges, key=lambda k:k[2])
        # 1.create MST : get min weight
        val = 0
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                val += edge[2]
        print(val)
        print(uf.numComponent)

if __name__ == '__main__':
    n = 5
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    Solution().findCriticalAndPseudoCriticalEdges(n, edges)