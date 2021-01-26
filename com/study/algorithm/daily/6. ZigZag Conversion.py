
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[] for i in range(numRows)]
        directions = [(1,0),(-1,1)]
        flag = 0 # 0, 1
        for i in range(len(s)):

            while flag == 0:
                if i + directions[flag][0] < numRows:
                    res[i % numRows].append(s[i])
                    i += 1
                else:
                    flag = 1
            j = numRows - 1 - 1
            while flag == 1:
                if 0 < i + directions[flag][0] and j  :



if __name__ == '__main__':
    string = "PAYPALISHIRING"
    print(len(string))