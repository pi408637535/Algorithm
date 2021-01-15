
#拓扑排序
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """''
        # 先导课为key，后续课为list
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        for ele in prerequisites:
            graph[ele[1]].append(ele[0])
            in_degree[ele[0]] += 1

        queue = collections.deque([i for i in range(len(in_degree)) if in_degree[i] == 0])
        res = 0
        while queue:
            node = queue.popleft()
            res += 1
            for ele in graph[node]:
                in_degree[ele] -= 1
                if not in_degree[ele]:
                    queue.append(ele)
        return  True if res == numCourses else False


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.if_loop = False
        self.graph = collections.defaultdict(list)
        for ele in prerequisites:
            self.graph[ele[1]].append(ele[0])

        # 0 not visited, 1 visiting, 2 visited
        self.visited = [0] * numCourses
        self.order = []

        for node in range(numCourses):
            if not self.if_loop and self.visited[node] == 0:
                self.dfs(node)
        return not self.if_loop

    def dfs(self, node):
        # nonlocal if_loop
        self.visited[node] = 1
        for neighbour in self.graph[node]:
            if self.visited[neighbour] == 0:
                self.dfs(neighbour)
                if self.if_loop:
                    return
            elif self.visited[neighbour] == 1:
                self.if_loop = True
                return
        self.visited[node] = 2
        self.order.append(node)

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    prerequisites = [[0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))