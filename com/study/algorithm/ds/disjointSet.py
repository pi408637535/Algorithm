
class DisjointSet():
    def __init__(self, vertices):
        m = len(vertices)
        self.parent = [-1] * m #-1 stand init

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并成功1，失败0
    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx != parenty:
            pass

if __name__ == '__main__':
    vertices = [
        [0,1],[1,2],[1,3],[2,4],[3,4],[2,5]
    ]
