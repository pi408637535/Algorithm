class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
        f = [[0 for j in range(3)] for i in range(len(costs))]

        for i in range(len(costs)):
            if i == 0:
                f[i][0] = costs[i][0]
                f[i][1] = costs[i][1]
                f[i][2] = costs[i][2]
            else:
                f[i][0] = min(f[i-1][1], f[i-1][2]) + costs[i][0]
                f[i][1] = min(f[i - 1][0], f[i - 1][2]) + costs[i][1]
                f[i][2] = min(f[i - 1][1], f[i - 1][0]) + costs[i][2]

        return min(f[-1])


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
        # f = [[0 for j in range(3)] for i in range(len(costs))]
        pre,now = [0] * 3, [0] * 3

        for i in range(len(costs)):
            pre = now.copy() #深浅拷贝的问题
            if i == 0:
                now[0] = costs[i][0]
                now[1] = costs[i][1]
                now[2] = costs[i][2]
            else:
                now[0] = min(pre[1], pre[2]) + costs[i][0]
                now[1] = min(pre[0], pre[2]) + costs[i][1]
                now[2] = min(pre[1], pre[0]) + costs[i][2]

        return min(now)



if __name__ == '__main__':
    costs = [[14,2,11],[11,14,5],[14,3,10]]
    # costs = [[1,2,3]]
    print(Solution().minCost(costs))
