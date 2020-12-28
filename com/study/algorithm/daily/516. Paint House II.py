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
        f = [ [0 for j in range(k)] for i in range(n + 1)]

        for i in range(1, n + 1):

            min_num = sys.maxsize
            for j in range(k):
                for c in range(k):
                    if c != j:
                        min_num = min(min_num, f[i-1][j] + costs[i-1][j])

                f[i][j] = min_num

        return min(f[-1])

if __name__ == '__main__':
    costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    print(Solution().minCostII(costs))