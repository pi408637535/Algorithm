class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False


        factors = [2,3,5]

        for ele in factors:
            while num % ele == 0:
                num = num // ele

        if num == 1:
            return True
        else:
            return False



if __name__ == '__main__':
    num = 8
    print(Solution().isUgly(1))