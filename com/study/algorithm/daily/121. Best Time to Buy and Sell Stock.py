class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        min_num = prices[0]
        res = 0
        for ele in prices:
            res = max(res, ele - min_num)
            min_num = min(min_num, ele)

        return res



if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))