class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        f = [0 for i in range(num + 1)]
        
        f[0] = 0
        
        for i in range(num + 1):
            if i == 0: continue
            #转移方程固定
            f[i] = f[i >> 1] + (i & 1)

        return f


if __name__ == '__main__':
    data = 5

    print( Solution().countBits(data) )