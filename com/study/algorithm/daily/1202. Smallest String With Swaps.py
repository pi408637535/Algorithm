import collections
#思路： 同一深林的排序
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graph = collections.defaultdict(dict)
        for ele in pairs:
            graph[ele[0]][ele[1]] = True
            graph[ele[1]][ele[0]] = True

        self.graph = graph
        self.used = set()

        res = []
        s = [ele for ele in s]
        self.s = s
        for index,ele in enumerate(s):
            min_ele = self.dfs(index, set())
            s[index],s[min_ele] = s[min_ele], s[index]
            self.used.add(index)
            res.append(s[min_ele])
        return res

    def dfs(self, index, visited):

        for ele in self.graph[index]:
            if self.if_visited(ele) and ele not in visited:
                visited.add(ele)
                if ord(self.s[index]) < ord(self.s[ele]):
                    self.dfs(index, visited)
                else:
                    index = ele
                    self.dfs(ele, visited)

        return index


    def if_visited(self, ele):
        if ele in self.used:
            return False
        return True

import collections
class Solution:

    def dfs(self, i, is_connected):
        for neighbour in self.graph[i]:
            if neighbour not in self.visited:
                # is_connected.append(self.s[neighbour])
                is_connected.append(neighbour)
                self.visited.add(neighbour)
                self.dfs(neighbour, is_connected)

    def smallestStringWithSwaps(self, s, pairs):
        # 建图
        graph = collections.defaultdict(list)
        for ele in pairs:
            graph[ele[0]].append(ele[1])
            graph[ele[1]].append(ele[0])
        self.graph = graph
        self.visited = set()
        self.s = s

        # print(self.graph)

        res = list(s)
        for i in range(len(s)):
            if i not in self.visited:
                is_connected = []
                self.dfs(i, is_connected)
                neighbour = [s[i] for i in is_connected]
                neighbour.sort()
                is_connected.sort()
                for j,ele in zip(is_connected, neighbour):
                    res[j] = ele
        return "".join(res)

class Solution(object):

    def bfs(self, i, is_connected):
        if i not in self.visited:
            self.visited.add(i)
            is_connected.append(i)
            queue = collections.deque(self.graph[i])

            while queue:
                node = queue.popleft()
                if node not in self.visited:

                    self.visited.add(node)
                    is_connected.append(node)
                    queue.extend(self.graph[node])


    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        for ele in pairs:
            graph[ele[0]].append(ele[1])
            graph[ele[1]].append(ele[0])
        self.graph = graph
        self.visited = set()
        self.s = s

        res = list(s)
        for i in range(len(s)):
            if i not in self.visited:
                is_connected = []
                self.bfs(i, is_connected)
                neighbour = [s[i] for i in is_connected]
                neighbour.sort()
                is_connected.sort()
                for j, ele in zip(is_connected, neighbour):
                    res[j] = ele
        return "".join(res)




if __name__ == '__main__':
    # s = "dcab"
    # pairs = [[0,3],[1,2]]
    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    print(Solution().smallestStringWithSwaps(s, pairs))
