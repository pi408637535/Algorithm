class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        string_n = str(N)
        flag = False
        for i in range(1, len(string_n)):
            if ord(string_n[i- 1]) > ord(string_n[i]):
                flag = True
                break
        if not flag:
            return N
        else:
            # 332 299
            # 1231 1299



            res = string_n[:i - 1]
            res += chr(ord(string_n[i - 1]) - 1)
            res += '9' * (len(string_n) - i)
            return int(res)


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        string_n = str(N)
        max_num = -1 #最大当前最大的数，与index联用
        index = -1 #标识位来解决 3332，这种带重复的数字，记录首个最大值
        flag = False #判断是否是monotone increasing digits
        for i in range(len(string_n)):
            if int(string_n[i]) >= max_num:
                if int(string_n[i]) > max_num: index = i
                max_num = int(string_n[i])

            else:
                flag = True
                break

        if not flag:
            return N
        else:
            res = string_n[:index]
            res += chr(ord(string_n[index] ) - 1)
            res += '9' * (len(string_n) - index - 1)
            return int(res)

if __name__ == '__main__':

    # N = 9
    # N = 1234
    # N = 332
    # N = 54
    # N = 1201
    # N = 110
    # N = 8
    # N = 132

    print(Solution().monotoneIncreasingDigits(N))