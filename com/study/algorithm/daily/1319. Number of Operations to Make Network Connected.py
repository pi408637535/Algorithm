import numpy as np


class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_redundant = 0
        self.conn_set = set()  # 仅记录现有中心点

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Two point merge
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            self.num_redundant += 1
            return False
        else:
            self.parent[parent_y] = parent_x
            self.conn_set.add(parent_x)
            return True

    def allCentralNodeNum(self, n):
        num = 0
        for i in range(n):
            if self.find(i) == i:
                num += 1
        return num


import numpy as np


class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_redundant = 0
        self.num_conned = n  # 连通分量总数

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Two point merge
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            self.num_redundant += 1
            return False
        else:
            self.parent[parent_y] = parent_x
            self.num_conned -= 1
            return True


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)

        for ele in connections:
            uf.union(ele[0], ele[1])
        if uf.num_redundant + 1 >= uf.num_conned:
            return uf.num_conned - 1
        else:
            return -1


if __name__ == '__main__':
    # n = 4
    # connections = [[0, 1], [0, 2], [1, 2]]

    # n = 6
    # connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]

    # n = 6
    # connections = [[0, 1], [0, 2], [0, 3], [1, 2]]

    n = 5
    connections = [[0, 1], [0, 2], [3, 4], [2, 3]]

    # n = 100
    # connections = [[17,51],[33,83],[53,62],[25,34],[35,90],[29,41],[14,53],[40,84],[41,64],[13,68],[44,85],[57,58],[50,74],[20,69],[15,62],[25,88],[4,56],[37,39],[30,62],[69,79],[33,85],[24,83],[35,77],[2,73],[6,28],[46,98],[11,82],[29,72],[67,71],[12,49],[42,56],[56,65],[40,70],[24,64],[29,51],[20,27],[45,88],[58,92],[60,99],[33,46],[19,69],[33,89],[54,82],[16,50],[35,73],[19,45],[19,72],[1,79],[27,80],[22,41],[52,61],[50,85],[27,45],[4,84],[11,96],[0,99],[29,94],[9,19],[66,99],[20,39],[16,85],[12,27],[16,67],[61,80],[67,83],[16,17],[24,27],[16,25],[41,79],[51,95],[46,47],[27,51],[31,44],[0,69],[61,63],[33,95],[17,88],[70,87],[40,42],[21,42],[67,77],[33,65],[3,25],[39,83],[34,40],[15,79],[30,90],[58,95],[45,56],[37,48],[24,91],[31,93],[83,90],[17,86],[61,65],[15,48],[34,56],[12,26],[39,98],[1,48],[21,76],[72,96],[30,69],[46,80],[6,29],[29,81],[22,77],[85,90],[79,83],[6,26],[33,57],[3,65],[63,84],[77,94],[26,90],[64,77],[0,3],[27,97],[66,89],[18,77],[27,43]]
    print(Solution().makeConnected(n, connections))