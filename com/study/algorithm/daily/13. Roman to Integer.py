
#栈:利用栈获取各个确切的罗马字母，然后在逐位计算栈中元素

import collections
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        romn = collections.OrderedDict()
        romn["M"] = 1000
        romn["CM"] = 900
        romn["D"] = 500
        romn["CD"] = 400
        romn["C"] = 100
        romn["XC"] = 90
        romn["L"] = 50
        romn["XL"] = 40
        romn["X"] = 10
        romn["IX"] = 9
        # romn["VIII"] = 8
        # romn["VII"] = 7
        # romn["VI"] = 6
        romn["V"] = 5
        romn["IV"] = 4
        romn["I"] = 1

        stack = []
        n = len(s)
        stack.append(s[0])
        for i in range(1,n):
            if s[i-1:i+1] in romn:
                stack.pop()
                stack.append(s[i-1:i+1])
            else:
                stack.append(s[i])

        res = 0
        for ele in stack:
            res += romn[ele]
        return res


if __name__ == '__main__':
    s = "LVIII"
    s = "MCMXCIV"
    s = "LVIII"
    s = "IX"
    s = "III"
    s = "IV"
    print(Solution().romanToInt(s))
