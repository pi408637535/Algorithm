class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0


        f = [0 for i in range(len(prices))]


        for i in range(1, len(prices)):

            f[i] = max([prices[i] - min(prices[:i]), f[i]])

        return max(f)

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    prices = []

    print( Solution().maxProfit(prices) )
