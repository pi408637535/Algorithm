class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        f = [0 for i in range(len(prices) + 1)]

        for i in range(1, len(prices)):
           f[i] = prices[i] - min(prices[:i])

        return max(f)


if __name__ == '__main__':
    data = [7,6,4,3,1]
    print( Solution().maxProfit(data) )