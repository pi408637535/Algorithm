
class DisjointSet():
    def __init__(self, isConnected):
        m, n = len(isConnected), len(isConnected[0])
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0

        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            self.count -= 1

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        m, n = len(isConnected), len(isConnected[0])
        if not m or not n:
            return n

        uf = DisjointSet(isConnected)

        direction = [(0,1), (1,0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    for ele in direction:
                        r,c = ele[0],ele[1]
                        if 0 <= i + r < m and 0 <= j + c < n and isConnected[i + r][j + c]:
                            uf.union(i * n + j, r * n + c)


        return uf.count


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().findCircleNum(isConnected))
