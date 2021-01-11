import collections
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


if __name__ == '__main__':
    # s = "dcab"
    # pairs = [[0,3],[1,2]]
    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    print(Solution().smallestStringWithSwaps(s, pairs))
