
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

#DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.visited = set()

        return sum( [ self.floodFillDfs(i,j)  for i in range(self.m) for j in range(self.n)] )

    def floodFillDfs(self, x, y):
        if not self._isValid(x, y):
            return 0
        self.visited.add((x,y))
        for d in [(1,0), (0,1), (-1,0), (0, -1)]:
            self.floodFillDfs(x + d[0], y + d[1])
        return 1

    def _isValid(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False

        if self.grid[x][y] == '0' or (x,y) in self.visited:
            return False
        return True

#BFS
import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.visited = set()

        return sum( [ self.floodFill_BFS(i,j)  for i in range(self.m) for j in range(self.n)] )

    def floodFill_BFS(self, x, y):
        if not self._isValid(x, y):
            return 0

        self.visited.add((x,y))
        queue = collections.deque()
        queue.append((x,y))

        while queue:
            cur_x, cur_y = queue.popleft()
            for d in [(1,0), (0,1), (-1,0), (0, -1)]:
                new_x, new_y = cur_x + d[0], cur_y + d[1]
                if self._isValid(new_x, new_y):
                    self.visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return 1

    def _isValid(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False

        if self.grid[x][y] == '0' or (x,y) in self.visited:
            return False
        return True

#2021.1.8
import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0

        self.m, self.n = len(grid),len(grid[0])
        self.visited = set()
        self.grid = grid
        self.queue = collections.deque()


        res = []
        for i in range(self.m):
            for j in range(self.n):
                res.append(self._bfs(i,j))
        return sum(res)

    def _dfs(self, i, j):
        if self._isValid(i,j):
            self.visited.add( (i,j) )
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                self._dfs(i + d[0], j + d[1])
            return 1
        else:
            return 0

    def _bfs(self, i, j):
        if self._isValid(i,j):
            self.visited.add( (i,j) )
            self.queue.append( (i,j) )

            while self.queue:
                cur_x, cur_y = self.queue.popleft()
                for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_x, new_y = cur_x + d[0], cur_y + d[1]
                    if self._isValid(new_x, new_y):
                        self.visited.add((new_x, new_y))
                        self.queue.append((new_x, new_y))
            return 1
        else:
            return 0

    def _isValid(self, i, j):

        # if 0 <= i < self.m and 0 <= j < self.n:
        #     if (i,j) not in self.visited and self.grid[i][j] == "1":
        #         return True
        #     else:
        #         return False
        # else:
        #     return False
        if not(0 <= i < self.m and 0 <= j < self.n):
            return False
        if (i,j) in self.visited or self.grid[i][j] != "1":
            return False

        return True





if __name__ == '__main__':
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]


    print(Solution().numIslands(grid))


if __name__ == '__main__':

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]

    print(Solution().numIslands(grid))
