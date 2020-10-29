import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        f = [0] * (amount+1)

        for ele in coins:
            if ele <= amount:
                f[ele] = 1

        for i in range(1,amount + 1):
            min_num = sys.maxsize
            for ele in coins:
                if i - ele >= 0:
                    min_num = min(min_num, f[i-ele])
            f[i] = min_num + 1
        if f[amount] == 0 or f[amount] > sys.maxsize:
            return  -1
        else:
            return f[amount]

if __name__ == '__main__':
    # coins = [1, 2, 5]
    # amount = 11
    coins = [2]
    amount = 1

    print(Solution().coinChange(coins, amount))

