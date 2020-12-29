class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        state = 2
        f = [[0 for j in range(state) ] for i in range(len(prices))]
        f[0][1] = -prices[0]

        for i,ele in enumerate(prices):

            if i == 0:
                f[i][1] = ele
            else:
                f[i][0] = max(f[i - 1][0], f[i - 1][1] + ele - fee)
                f[i][1] = max(f[i - 1][1], f[i - 1][0] - ele)

        return f[i - 1][0]

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print( Solution().maxProfit(prices, fee) )