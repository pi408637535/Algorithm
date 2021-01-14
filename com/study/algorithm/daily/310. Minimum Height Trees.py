import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        degree = [0] * n  # 入度
        graph = collections.defaultdict(list)

        for ele in edges:
            graph[ele[0]].append(ele[1])
            graph[ele[1]].append(ele[0])
            degree[ele[0]] += 1
            degree[ele[1]] += 1

        queue = collections.deque([i for i in range(n) if degree[i] == 1])
        visited = set()
        node = None
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return node


if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(Solution().findMinHeightTrees(n, edges))



