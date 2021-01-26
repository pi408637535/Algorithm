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


class UnionFind():
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_y != parent_x:
            self.parent[parent_y] = parent_x
            self.count -= 1
            return True
        else:
            return False


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        size = n * n * 4
        uf = UnionFind(size)

        for i in range(n):
            for j in range(n):
                # index = i * n + j #定位所在格
                index = 4 * (i * n + j) # 4*(i * n + j)才能确定每个格子，因为一个格子在画成4小份

                # 格内合并 merge=0,1 merge=2,3
                sign = list(grid[i])[j]
                if sign == "/":
                    uf.union(index, index + 3)
                    uf.union(index + 1, index + 2)
                elif sign == '\\':
                    uf.union(index, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)

                #相邻格合并 右 + 下
                if j + 1 < n:
                    uf.union(index + 1, 4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    uf.union(i * n + j + 2, (i+1) * n * 4 + j )

                uf.count

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
