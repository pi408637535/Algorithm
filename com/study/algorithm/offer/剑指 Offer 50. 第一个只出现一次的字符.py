
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ele in s:
           dic[ele] = dic.get(ele, 0) + 1


        for ele in s:
            if dic[ele] == 1:
                return ele

        return " "

if __name__ == '__main__':
    s = "abaccdeff"
    s = ""
    print( Solution().firstUniqChar(s) )