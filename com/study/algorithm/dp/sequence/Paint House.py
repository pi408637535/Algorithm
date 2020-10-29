class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        n = len(costs)

        f = [ [0 for j in range(3)] for i in range(n) ]

        for i in range(n):
            f[i][0] = min([ f[i-1][1], f[i-1][2] ]) + costs[i][0]
            f[i][1] = min([f[i - 1][0], f[i - 1][2]]) + costs[i][1]
            f[i][2] = min([f[i - 1][1], f[i - 1][0]]) + costs[i][2]

        return min(f[-1])

if __name__ == '__main__':
    costs =  [[14,2,11],[11,14,5],[14,3,10]]
    print( Solution().minCost(costs) )
