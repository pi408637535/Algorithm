#最小生成树、并查集、

#最小生成树可用bfs

# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def minimumEffortPath(self, heights) -> int:
        #先按照边进行排序
        edges = []
        if not heights or not heights[0]:
            return 0
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                node = i * n + j
                if i > 0: #up
                    edges.append( ( (i - 1) * n + j,  node, abs(heights[i][j] - heights[i - 1][j])) )
                if j > 0:
                    edges.append( ( (i) * n + j - 1, node, abs(heights[i][j] - heights[i][j - 1])) )
        edges = sorted(edges, key=lambda x: x[2])

        if not edges:
            return 0

        uf = UnionFind(m * n)

        distance = 0
        for ele in edges:
            uf.unite(ele[0],ele[1])
            distance = max(distance, ele[2])
            if uf.connected(0, m * n - 1):
                return distance

if __name__ == '__main__':
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    heights = [[3]]
    print(Solution().minimumEffortPath(heights))
