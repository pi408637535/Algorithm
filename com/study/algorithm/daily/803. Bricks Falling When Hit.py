
class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x]

    def getSize(self, x):
        return self.size[self.find(x)]

import copy
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])

        #first, 把grid中砖头全部击碎
        # copy_grid = [[0] * cols for i in range(rows) ]
        copy_grid = copy.deepcopy(grid)
        for hit in hits:
            copy_grid[hit[0]][hit[1]] = 0

        #second 砖块间连接信息
        size = rows * cols
        uf = UnionFind(size + 1 ) # +1表示屋顶

        for j in range(cols):
            if copy_grid[0][j] == 1:
                uf.union(j, size)

        for i in range(1, rows):
            for j in range(cols):
                if copy_grid[i][j] == 1:
                    if copy_grid[i-1][j] == 1:
                        uf.union(i * cols + j, (i-1)* cols + j)
                    if j > 0 and copy_grid[i][j - 1] == 1:
                        uf.union(i * cols + j, i * cols + j - 1)

        #hits中的brick逆序放入grid中
        hit_len = len(hits)
        res = []
        for ele in hits[::-1]:
            x = ele[0]
            y = ele[1]

            if grid[x][y] == 0:
                res.append(0)
                continue

            origin = uf.getSize(size)

            #补回砖块
            if x == 0:
                uf.union(y, size)
            for direction in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < rows and 0 <= new_y < cols and copy_grid[new_x][new_y]:
                    uf.union(x * cols + y, new_x * cols + new_y)



            current = uf.getSize(size)
            res.append( max(0, current - origin - 1) )
            copy_grid[x][y] = 1

        return res[::-1]

if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]

    # grid = [[1, 0, 0, 0], [1, 1, 0, 0]]
    # hits = [[1, 1], [1, 0]]
    # grid = [[1], [1], [1], [1], [1]]
    # hits = [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]

    # grid =  [[1, 0, 1], [0, 0, 1]]
    # hits = [[1, 0], [0, 0]]

    grid = [[1,0,0,0],[1,1,0,0]]
    hits = [[1, 1], [1, 0]]
    print(Solution().hitBricks(grid, hits))