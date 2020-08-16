import math
import sys
class Solution(object):
    def strToInt(self, string):
        """
        :type str: str
        :rtype: int
        """

        string = string.strip()



        start_index = 0
        # for ele in string:
        #     if '0' <= ele and ele <='9' or ele == "-":
        #         break
        #     else:
        #         start_index += 1
        string = string[start_index:]
        if len(string) == 0:
            return 0

        flag = 1
        if string[0] == "-":
            flag = -1
            string = string[1:]
        elif string[0] == "+":
            flag = 1
            string = string[1:]

        max_num = 2 ** 31 -1
        res = 0
        i = 0
        for ele in string:

            if res >= max_num: return max_num  * flag

            if '0' <= ele and ele <= '9':
                res = res * 10 ** i + ord(ele) - ord('0')
            else:
                return flag * res

            i = 1 if i == 0 else 1

        return flag * res


if __name__ == '__main__':
    string = "3.14159"
    string = "words and 987"
    #string = "+1"
    string = '-'
    string = "2147483648"

    print(Solution().strToInt(string))