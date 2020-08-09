
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

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        #f = [0 for i in range(len(prices) + 1)]

        max_num = prices[0]
        min_num = sys.maxsize
        profit = 0
        for i in range(0, len(prices)):

            min_num = min([ prices[i], min_num ])
            profit = max(profit, prices[i] - min_num)

        return profit

if __name__ == '__main__':
    data = [4]
    print( Solution().maxProfit(data) )