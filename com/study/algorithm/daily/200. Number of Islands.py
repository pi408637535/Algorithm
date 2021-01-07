
class DisjointSet():

    def __init__(self, data):
        m,n = len(data), len(data[0])
        self.count = 0
        self.parent = [[-1] * n] * m
        self.rank = [[0] * n] * m

        # self.parent = [-1] * (m * n)
        # self.rank = [0] * (m * n)

        for i in range(m):
            for j in range(n):
                if data[i][j] == '1':
                    self.parent[i][j] = i * n + j
                    # self.parent[i * n + j] = i * n + j
                    # self.count += 1

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    # def find(self, i):
    #     if self.parent[i] != i:
    #         self.parent[i] = self.find(self.parent[i])
    #     return self.parent[i]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            else:
                self.parent[parent_x] = parent_y
                self.rank[parent_x] += 1
            self.count -= 1


class Solution(object):
    def numIslands(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        if not isConnected or not isConnected[0]:
            return 0

        uf = DisjointSet(isConnected)
        direction = [(0,1), (0,-1), (1,0), (-1, 0)]
        m, n = len(isConnected), len(isConnected[0])

        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == '0':
                    continue
                for d in direction:
                    r,c = i + d[0], j + d[1]
                    if r >= 0 and c >= 0 and r < m and c < n and isConnected[r][c] == '1':
                        uf.union(i * n + j, r * n + c)

        return uf.count

if __name__ == '__main__':
    # isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    # isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # print(Solution().findCircleNum(isConnected))
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(Solution().numIslands(grid))
