
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[] for i in range(numRows)]

        index = 0
        length = len(s)
        while index < length:
            i = 0
            while i < numRows and index < length: #只要是和数组相关就要确保不越界。这是个编程习惯
                res[i].append(s[index])
                index += 1
                i += 1

            i = numRows - 2 #规律： 2-0，3-1，4-2，5-3
            while 0 < i and index < length: #这里需要确保 i > 0,因为只有这样才能确保方向进入向下的模式
                res[i].append(s[index])
                i -= 1
                index += 1

        content = []
        for i in range(numRows):
            content.append("".join(res[i]))

        return "".join(content)



if __name__ == '__main__':
    string = "PAYPALISHIRING"
    numRows = 4
    #"PINALSIGYAHRPI"
    print(Solution().convert(string, numRows))