'''
    作弊模型：今天知道明天的价格
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        if len(prices) == 0:
            return 0
        old = prices[0]

        for index,ele in enumerate(prices):
            if index == 0: continue
            if ele > prices[index-1]:
                profit += ele - prices[index-1]


        return profit



if __name__ == '__main__':
    data = [1,2,3,4,5]
    print( Solution().maxProfit(data) )