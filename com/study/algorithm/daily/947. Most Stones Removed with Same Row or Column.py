class DisjointSetUnion:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            return x
        elif self.parent[x] == x:
            return self.parent[x]
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            self.parent[fx] = fy
        elif self.rank[fy] < self.rank[fx]:
            self.parent[fy] = fx
        else:
            self.parent[fy] = fx
            self.rank[fx] += 1

    def numberOfConnectedComponent(self):
        return sum(1 for x, fa in self.parent.items() if x == fa)


#finial,all node will stand on different row,columns
#same row or same column are in same space ,so we need to project them.
#this is a great idea, code is: x + size,y
class Solution:
    def removeStones(self, stones) -> int:
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.union(x, y + 10001)
        return len(stones) - dsu.numberOfConnectedComponent()


if __name__ == '__main__':
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    # stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    # stones = [[0, 0]]
    print(Solution().removeStones(stones))