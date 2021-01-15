import collections

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]

        degree = [0] * n  # 入度存储表
        graph = collections.defaultdict(list) #构建图

        for ele in edges:
            graph[ele[0]].append(ele[1])
            graph[ele[1]].append(ele[0])
            degree[ele[0]] += 1
            degree[ele[1]] += 1

        queue = collections.deque([i for i in range(n) if degree[i] == 1])
        visited = set()
        # node = None
        while queue:
            res = []
            #一次性弹出入度相同的节点
            size = len(queue) #消减位于同一层的节点
            for i in range(size):
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    res.append(node)
                    for neighbor in graph[node]:
                        degree[neighbor] -= 1

                        if degree[neighbor] == 1:
                            queue.append(neighbor)
        return res


if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(Solution().findMinHeightTrees(n, edges))



