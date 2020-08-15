class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        valid = { str(i):True for i in range(26) }
        num = str(num)
        f = [0 for i in range(len(num) + 1)]
        f[0] = 1
        for i in range(1, len(num)+1):
            temp = 0
            if i - 2 >= 0 and valid.get(num[i-2:i]):
                temp = f[i - 2]
            
            f[i] = f[i-1] + temp
                
        return f[len(num)]


if __name__ == '__main__':
    #num = 26
    num = 12258
    print( Solution().translateNum(num) )