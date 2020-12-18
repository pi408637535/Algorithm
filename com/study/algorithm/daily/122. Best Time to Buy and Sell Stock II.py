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


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        f = [[ 0 for j in range(2)] for i in range(len(prices))]
        f[0][1] = -prices[0]

        for index, ele in enumerate(prices):
            if index == 0:
                f[index][1] = -ele
            else:
                f[index][0] = max(f[index - 1][0], f[index-1][1] + ele)
                f[index][1] = max(f[index - 1][1], f[index-1][0] - ele)

        return f[index][0]

if __name__ == '__main__':
    princes = [7,1,5,3,6,4]
    print(Solution().maxProfit(princes))