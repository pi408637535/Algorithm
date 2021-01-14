
# 并查集
# 本质问题:树形成环的最后那条边
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes_num = len(edges) + 1
        self.parent = list(range(nodes_num))
        self.rank = list(range(nodes_num))

        for x,y in edges:
            parent_x, parent_y = self.find(x), self.find(y)
            if parent_x != parent_y:
                self.union(parent_x, parent_y)
            else:
                return [x,y]
        return []

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    '''
    x,y 在这里都是指代x,y的parent
    :param x: 
    :param y: 
    :return: 
    '''
    def union(self,x, y):
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[y] < self.rank[x]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

if __name__ == '__main__':
    edges = [[1,2], [1,3], [2,3]]
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(Solution().findRedundantConnection(edges))