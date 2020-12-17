class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        res = 0
        pre = prices[0]
        for ele in prices:
            if ele - pre > 0:
                res += ele - pre
            pre = ele

        return res

if __name__ == '__main__':
    princes = [7,1,5,3,6,4]
    print(Solution().maxProfit(princes))