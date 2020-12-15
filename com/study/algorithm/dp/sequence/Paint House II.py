import sys

# N * K * K
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0

        k = len(costs[0])

        f = [ [0 for j in range(k)] for i in range(n)]

        for j in range(k):
            f[0][j] = costs[0][j]

        for i in range(1,n):
            for j in range(k): #前一个房子染色色彩
                min_value = sys.maxsize
                for m in range(k): #第i个房子染得色彩
                    if m != j:
                       min_value = min([min_value, f[i-1][m]])

                f[i][j] = min_value + costs[i][j]

        return min(f[-1])


class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0

        k = len(costs[0])

        f = [ [0 for j in range(k)] for i in range(n)]

        for j in range(k):
            f[0][j] = costs[0][j]

        for i in range(1,n):


            first_min = sys.maxsize
            second_min = sys.maxsize
            id1 = 0
            id2 = 0
            for j in range(k):  # 前一个房子染色色彩
                if f[i-1][j] < first_min:
                    second_min = first_min
                    id2 = id1
                    first_min = f[i-1][j]
                    id1 = j
                elif f[i-1][j] < second_min:
                    second_min = f[i-1][j]
                    id2 = j

            for j in range(k):
                f[i][j] = costs[i][j]
                if j != id1:
                    f[i][j] += first_min
                else:
                    f[i][j] += second_min

        return min(f[-1])


# 2020.10.31
import sys
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        length = len(costs)
        if not length:
            return 0
        k = len(costs[0])

        f = [[0 for j in range(k)]  for i in range(length + 1)]
        id1, id2 = 0,0

        for i in range(k):
            f[0][i] = 0

        for i in range(1, length+1):
            min1,min2 = sys.maxsize,sys.maxsize
            for j in range(k):
                if f[i - 1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = f[i - 1][j]
                    id1 = j
                elif f[i-1][j] < min2:
                    min2 = f[i-1][j]
                    id2 = j

            for j in range(k):
                f[i][j] = costs[i-1][j]
                if j != id1:
                    f[i][j] += min1
                else:
                    f[i][j] += min2



        return min(f[-1])




if __name__ == '__main__':
    costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    #costs = [[5]]
    print( Solution().minCostII(costs) )