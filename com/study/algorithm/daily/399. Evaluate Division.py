import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1 / v
        res = []
        self.graph = graph
        for m, n in queries:
            if m not in graph or n not in graph:
                res.append(-1)
            else:
                res.append(self._dfs(m, n, set()))

        return res

    def _dfs(self, x, y, visited):
        if x not in self.graph or y not in self.graph:
            return -1
        if x == y:
            return 1
        visited.add(x)
        for ele in self.graph[x]:
            if ele not in visited:
                v = self._dfs(ele, y, visited)
                if v != -1:
                    return self.graph[x][ele] * v

        return -1


#并查集 高度为2
#有错误但是不调试了，对并查集还不熟悉
#错题前还是要先把题目在纸上画明白了，才方便开动
class UnionFind():
    def __init__(self, size):
        self.parent = [ i for i in range(size)]
        self.weights = [1] * size #指向父节点的权值

    #value：有向边的权值
    def union(self, x, y , value):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        self.parent[parent_x] = parent_y
        self.weights[parent_x] = self.weights[parent_y] * value / self.weights[parent_x]

    def find(self, x):
        if x != self.parent[x]:
            original = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weights[x] *= self.weights[original]
        return self.parent[x]

    def isConnected(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return self.weights[x] / self.weights[y]
        else:
            return -1

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        n = len(equations)
        uf = UnionFind(n * 2)
        hash_map = {} #记录是否存储了各个元素
        id = 0 #用于记录各个元素的位置
        for (x,y),v in zip(equations, values):
            if x not in hash_map:
                hash_map[x] = id
                id += 1

            if y not in hash_map:
                hash_map[y] = id
                id += 1

            uf.union(hash_map[x], hash_map[y], v)

        res = []
        for ele in queries:
            id1 = hash_map.get(ele[0])
            id2 = hash_map.get(ele[1])

            if id1 == None or id2 == None:
                res.append(-1)
            else:
                res.append(uf.isConnected(id1, id2))
        return res


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, queries))
