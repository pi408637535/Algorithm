class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {} # '1'-> a
        for i in range(1, 27):
            dic[str(i)] = chr( i + ord('a') )

        f = [[ 0 for j in range(2)]  for i in range(len(s) + 1)]
        for i in range( 1, len(s) + 1 ):
            if i == 1:
               f[i][0] = 1 if s[i - 1] in dic else 0
            else:
                if s[i-1:i] in dic:
                    f[i][0] = max(f[i-1][0], f[i-1][1])
                if s[i-2:i] in dic:
                    f[i][1] = max(f[i-2][0], f[i-2][1])


        return f[-1]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 1
        f = [0] * len(s)

        dic = {}  # '1'-> a
        for i in range(1, 27):
            dic[str(i)] = chr(i + ord('a'))

        f = [0] * (len(s) + 1)
        f[0] = 1

        for i in range(1, len(s) + 1):
            f[i] = 0
            if ord('1') <= ord(s[i-1])  and ord(s[i-1]) <= ord('9'):
                f[i] += f[i - 1]

            if i > 1:
                j = 10 * ( ord(s[i-2]) - ord('0') ) + ord(s[i-1]) - ord('0')
                if 10 <= j and j <= 26:
                    f[i] += f[i - 2]

        return f[-1]


class Solution(object):
    def numDecodings(self, s):
        """
        转移方程：
            对于一个digit满足1-9时，f[i] = f[i-1]
            对于连续的两个字母满足10-24时， f[i] = f[i-1] + f[i-2]
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        f = [0] * (len(s) + 1)

        f[0] = 1 #创建这个初始条件，主要是因为方便转移方程
        for i in range(1, len(s) + 1):
            temp = ord(s[i-1]) - ord('0')
            if temp > 0 and temp < 10:
                f[i] = f[i-1]
            if i > 1:
                temp = 10 * ( ord(s[i-2]) - ord('0') ) + ( ord(s[i-1]) - ord('0') )
                if 10 <= temp and temp <= 26:
                    f[i] += f[i - 2]

        return f[-1]




if __name__ == '__main__':
    # s = "12"
    # s = "226"
    # s = "0"
    # s = "012"
    # s = "1"
    s = "10"


    print(Solution().numDecodings(s))
