#拓扑排序
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for ele in graph[node]:
                in_degree[ele] -= 1
                if not in_degree[ele]:
                    queue.append(ele)
        return res if len(res) == numCourses else []

if __name__ == '__main__':
    # numCourses = 2
    # prerequisites = [[1, 0]]
    # prerequisites = [[0, 1]]

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    numCourses = 3
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    print(Solution().findOrder(numCourses, prerequisites))