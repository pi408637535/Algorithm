import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [ 0 for i in range(amount + 1)]
        f[0] = 0

        for i in range(1, amount+1):
            min_amounts = []
            for coin in coins:
                coin_select = f[i - coin] if i - coin >= 0 else sys.maxsize
                min_amounts.append(coin_select)
            f[i] = min(min_amounts) + 1

        return  f[amount] if f[amount] < sys.maxsize else -1
        

if __name__ == '__main__':
    coins = [2, 5, 7]
    amount = 27
    
    print( Solution().coinChange(coins, amount) )