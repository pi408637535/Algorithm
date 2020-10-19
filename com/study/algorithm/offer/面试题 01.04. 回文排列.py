class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for ele in s:
            if ele not in dic:
                dic[ele] = 1
            else:
                del dic[ele]

        if len(dic) <= 1:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "tactco"
    s = "aaa"
    print( Solution().canPermutePalindrome(s) )