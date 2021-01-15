#思路：dfs
'''
    output degrees is zero is  terminial node
'''
import collections
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        degree = [0] * n
        tree = collections.defaultdict(list)
        for i,ele in enumerate(graph):
            for j in ele:
                tree[i].append(j)
                degree[i] += 1

        # print(tree)
        # print(degree)
        terminal = [i for i in range(len(degree)) if degree[i] == 0]

        self.termianl = terminal
        self.tree = tree

        res = []
        for node in range(n):
            flag = self.dfs(node, set(), node)
            if flag:
                res.append(node)
        res.sort()
        return res


    '''
        利用dfs,来统计同 i->terminal的步数
        node 节点索引
        visited 控制重复
        flag if is safe
    '''
    def dfs(self, node, visited, times):
        if node in self.termianl and times > 0:
            return True
        if times <= 0:
            return False

        visited.add(node)
        for neighbour in self.tree[node]:
            if neighbour not in visited:
                times -= 1
                flag = self.dfs(neighbour, visited, times)
                if flag:
                    return flag
                times += 1

        return flag


#坑，题意尽然是判断一个点最终是否会步入环中

#拓扑排序：判断是否有边。将所有边反向，从无环节点找到最底层节点
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        degree = [0] * n
        tree = collections.defaultdict(list)
        queue = collections.deque()
        for i, ele in enumerate(graph):
            for j in ele:
                tree[j].append(i) #边反向
                degree[i] += 1
            if not degree[i]:
                queue.append(i)

        # print(queue)
        # print(degree)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbour in tree[node]:
                degree[neighbour] -= 1
                if not degree[neighbour]:
                    queue.append(neighbour)

        return sorted(res)

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        degree = [0] * n # record degree
        tree = collections.defaultdict(list)
        for i, ele in enumerate(graph):
            for j in ele:
                tree[i].append(j)
                degree[i] += 1
        visited = [0] * n

        self.visited = visited
        self.tree = tree
        self.degree = degree

        res = []
        for i in range(n):
            if visited[i] == 0:
                flag = self.dfs(i)
                if not flag:
                    res.append(i)
        return res

    def dfs(self, node):

        if not self.degree[node]:
            return False

        if self.visited[node] == 1 and self.degree[node] != 0:
            return True
        else:
            self.visited[node] += 1
            for neighbour in self.tree[node]:
                if not self.degree[neighbour]:
                    return False
                self.visited[neighbour] += 1
                return self.dfs(neighbour)


if __name__ == '__main__':
    # graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    # graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    graph = [[],[0,2,3,4],[3],[4],[]]
    print(Solution().eventualSafeNodes(graph))