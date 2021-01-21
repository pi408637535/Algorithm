

#对点需要进行编号: (x,y) -> num
#最小生成树问题： 树定义 n个点，n-1条边
#krustal 边排序，(weight, x, y) 来解决通过最小边开始
class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            return True
        else:
            return False

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        manhattan = lambda x,y : abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        uf = UnionFind(n)
        length = []
        for i in range(n):
            for j in range(i + 1, n):
                length.append( (manhattan(i,j), i, j))

        length.sort()
        res = []
        for length,x,y in length:
            if uf.union(x, y):
                res.append(length)
                if len(res) == n - 1:
                    break

        return sum(res)

#prim 算法
import collections
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        # 构建邻接表
        graph = collections.defaultdict(dict)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                graph[i][j] = d
                graph[j][i] = d

        res = 0
        visited = set()
        dist = [float('inf')] * n
        dist[0] = 0
        # 构建最小生成树
        for i in range(n):
            min_ = float('inf')
            node = -1
            for j in range(n):
                if j not in visited and dist[j] < min_:
                    node = j
                    min_ = dist[j]
            visited.add(node)
            res += dist[node]
            for nex in graph[node]:
                if nex not in visited and graph[node][nex] < dist[nex]:
                    dist[nex] = graph[node][nex]
        return res


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(Solution().minCostConnectPoints(points))