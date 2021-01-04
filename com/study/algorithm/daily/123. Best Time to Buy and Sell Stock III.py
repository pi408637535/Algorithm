class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        f = [ [0 for j in range(4)] for i in range(len(prices) + 1) ]

        for i in range(1, len(prices) + 1):
            f[i][0] = -prices[i - 1]

            if f[i - 1][0]:
                f[i][1] = max(f[i-1][1], prices[i- 1] + f[i - 1][0])
            else:
                f[i][1] = f[i - 1][1]


            if f[i-1][1]:
                f[i][2] = max(f[i - 1][2], f[i - 1][1] - prices[i - 1])
            else:
                f[i][2] = f[i-1][1]

            if f[i - 1][2]:
                f[i][3] = max(f[i - 1][3], f[i - 1][2] + prices[i - 1])
            else:
                f[i][3] = f[i - 1][3]


        return max(f[-1])

if __name__ == '__main__':
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))
