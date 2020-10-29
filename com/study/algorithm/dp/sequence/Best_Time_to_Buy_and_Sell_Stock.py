class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        if len(prices) == 0:
            return profit

        min_data = prices[0]

        for index, ele in enumerate(prices):
            if index == 0: continue
            profit = max([ele - min_data, profit])
            min_data = min(prices[:index + 1])

        return profit



if __name__ == '__main__':
    data = [7,1,5,3,6,4]
    data = [2,1,4]
    print( Solution().maxProfit(data) )
