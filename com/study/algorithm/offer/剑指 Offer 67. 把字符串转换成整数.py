import math
import sys
class Solution(object):
    def strToInt(self, string):
        """
        :type str: str
        :rtype: int
        """
        number_char = []
        for i in range(0, 10):
            number_char.append(str(i))
        number_char.append("-")
        number_char.append(" ")

        number_str = []
        for ele in string:
            if ele in number_char:
                number_str.append(ele)

        total = 0
        flag = -1 if number_str[0] == '-' else 1
        number_str =  number_str if flag == 1 else number_str[1:]

        for index,ele in enumerate(number_str):
            total += math.pow(10,len(number_str) - 1 - index) * (ord(ele) - ord('0'))



        if total > pow(2, 31):
            return flag * int(pow(2, 31))
        else:
            return flag * int(total)




if __name__ == '__main__':
    string  =  "-91283472332"
    print(Solution().strToInt(string))