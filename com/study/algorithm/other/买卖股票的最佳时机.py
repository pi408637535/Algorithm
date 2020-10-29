class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_pre = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):

            max_profit = max(prices[i] - min_pre, max_profit)
            min_pre = min(min_pre, prices[i])

        return max_profit

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    print(Solution().maxProfit(nums))