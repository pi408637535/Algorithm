
class DisjointSet():
    def __init__(self, vertices):
        m = len(vertices)
        self.parent = [-1] * m #-1 stand init
        self.rank = [0] * m

    # def find(self, x):
    #     if self.parent[x] != -1:
    #         self.parent[x] = self.find(self.parent[x])
    #     return self.parent[x]

    # def find(self, x):
    #     if self.parent[x] != -1:
    #             self.parent[x] = self.find(self.parent[x])
    #     return x

    def find(self, x):
        x_root = x
        while self.parent[x_root] != -1:
                x_root = self.parent[x_root]
        return x_root

    # 合并成功1，失败0
    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx == parenty:
            return 0
        else:
            if self.rank[parentx] > self.rank[parenty]:
                self.parent[parenty] = parentx
            elif self.rank[parentx] < self.rank[parenty]:
                self.parent[parentx] = parenty
            else:
                self.parent[parentx] = parenty
                self.rank[parenty] += 1
            return 1


if __name__ == '__main__':
    vertices = [
        # [0,1],[1,2],[1,3],[3,4],[2,5],[2,4],
         [0,1],[1,2],[1,3],[2,4],[3,4]
    ]
    disjoint = DisjointSet(vertices)
    for i in range(len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]

        if disjoint.union(x, y) == 0:
            print("Cycle detected")
        else:
            print("No cycle detected")




