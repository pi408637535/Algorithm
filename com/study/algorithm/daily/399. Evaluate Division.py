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
        for (x,y),v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v



if __name__ == '__main__':
    dict1 = collections.defaultdict(2)
    print(dict1["a"])

