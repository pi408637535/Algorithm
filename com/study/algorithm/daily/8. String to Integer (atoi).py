class Solution(object):

    def str2num(self, s):
        s = s.strip()
        res = ""

        if not s:
            return '0'

        if s[0] == "+" or s[0] == "-":
            res += s[0]
            s = s[1:]

        num_set = [str(i) for i in range(10)]
        for ele in s:
            if ele in num_set:
                res += ele
            else:
                break
        return res

    def str2int(self, s):

        if not s:
            return 0

        res = 0
        flag = 1

        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            flag = -1

        num_dic = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

        for ele in s:
            print(type(res))
            res = int(res)
            if int(2147483647) < res or (res == 214748364 and ele > 7):
                return 2147483647
            elif res < -2147483648 or (res == -214748364 and ele < -8):
                return -2147483648
            res = res * 10 + num_dic[ele] * flag
        return res

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        #分两步：1.仅截取数字,截取不到就退出 2.转换数字
        string = self.str2num(s)
        return self.str2int(string)

if __name__ == '__main__':

    # string = "words and 987"
    # string = "4193 with words"
    string = "   -42"
    # string = "42"
    string = "-91283472332"
    string = ""
    string = "2147483646"
    print(Solution().myAtoi(string))
