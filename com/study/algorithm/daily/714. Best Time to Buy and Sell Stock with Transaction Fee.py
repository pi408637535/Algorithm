class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        res = 0
        pre = -1
        min_num = prices[0]
        for ele in prices:
            if ele - min_num > fee and min_num != pre:
                res += ele - min_num - fee
                pre = min_num

            min_num = min(min_num, ele)


        return res

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    prices = [1,3,7,5,10,3]
    fee = 3
    print(Solution().maxProfit(prices, fee))