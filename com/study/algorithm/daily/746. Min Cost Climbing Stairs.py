class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0

        f = [0] * (len(cost) + 1)

        for i in range(len(cost) + 1):
            if i == 0:
                f[i] = 0
            elif i == 1:
                f[i] = 0
            else:
                f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i - 2])

        return f[len(cost)]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0

        cur = 0
        pre = 0
        for i in range(2, len(cost) + 1):

            next_step = min(cur + cost[i - 1], pre + cost[i - 2])
            pre = cur
            cur = next_step

        return cur


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0

        f = [0] * (len(cost) + 1)


        pi = [0] * (len(cost) + 1) #用于保存dp转移的方向

        for i in range(len(cost) + 1):
            if i == 0:
                f[i] = 0
            elif i == 1:
                f[i] = 0
            else:
                f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i - 2])
                if f[i-1] + cost[i-1] < f[i-2] + cost[i - 2]:
                    pi[i - 1] = 1
                else:
                    pi[i-2] = 1

        pi[i] = 1
        path = [] #dp路径
        for i in range(len(pi)):
            if pi[i]:
                path.append(i)
        print(path)
        return f[len(cost)]

if __name__ == '__main__':
    cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))