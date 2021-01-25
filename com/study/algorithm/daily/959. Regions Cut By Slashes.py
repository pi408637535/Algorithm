class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_y] = parent_x
            self.count -= 1
        else:
            return


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        size = 4 * n * n

        uf = UnionFind(size)
        for i in range(n):
            row = list(grid[i])
            for j in range(n):
                index = 4 * (i * n + j)  #i * n + j:二维->一维.4 * (i * n + j)网格
                c = row[j]
                #格内合并
                if c == '/':
                    #merge 0、3， 1、2
                    uf.union(index, index + 3)
                    uf.union(index + 1, index + 2)
                elif c == '\\':
                    uf.union(index, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)

                #格外合并 右+下
                if j+1 < n:
                    uf.union(index+1, 4 * (i * n + j + 1)+3)
                if i + 1 < n:
                    uf.union(index + 2, 4 * ((i+1) * n + j ) )

        return uf.count

if __name__ == '__main__':
    grid = [
  " /",
  "/ "
    ]

    grid = [
        " /",
        "  "
    ]
    grid = [
        "\\/",
        "/\\"
    ]
    print(Solution().regionsBySlashes(grid))
