# time limit exceeded
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here

        n = len(costs)
        if not n:
            return 0
        k = len(costs[0])
        f = [ [0 for j in range(k)] for i in range(n + 1)]

        for i in range(1, n + 1):

            for j in range(k): # f[i][j] = min(f[i][k] + cost[i-1][j])
                temp = []
                for c in range(k): #
                    if c != j:
                        temp.append( f[i-1][c] + costs[i-1][j])

                f[i][j] = min(temp)

        return min(f[-1])

import sys
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if not n:
            return 0
        k = len(costs[0])
        f = [[0 for j in range(k)] for i in range(n + 1)]


        id1, id2 = None, None
        for i in range(1, n + 1):

            min1, min2 = sys.maxsize, sys.maxsize
            for c in range(k):
                if f[i-1][c] < min1:
                    min2 = min1 #要用最小替换次小
                    min1 = f[i-1][c]
                    id1 = c
                elif f[i-1][c] < min2:
                    min2 = f[i-1][c]
                    id2 = c

            for j in range(k):
                f[i][j] = costs[i-1][j]
                if j == id1:
                    f[i][j] +=  min2
                else:
                    f[i][j] += min1

        return min(f[-1])






if __name__ == '__main__':
    costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    # costs = [[1,2,3],[1,4,6]]
    costs = [[19,33,30],[30,26,14],[23,32,14],[21,16,32],[16,30,30],[15,18,30],[21,21,21],[23,30,15],[19,16,5],[17,20,30],[32,12,19],[18,8,31],[29,21,10],[2,9,13],[31,30,22]]
    print(Solution().minCostII(costs))