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


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_dic = {}
        for i in range(10):
            num_dic[str(i)] = chr(ord('a') + i)
        for i in range(11, 26):
            num_dic[str(i)] = chr(ord('a') + i)

        f = [1] * (len(str(num)))
        f[0] = 1


        for i in range(1,len(str(num))):
            if i == 1:
                temp = 1 if num_dic.get(str(num)[i-1:i+1]) else 0
                f[i] = f[i-1] + temp
            else:
                temp = f[i-2] if num_dic.get(str(num)[i-1:i+1]) else 0
                f[i] = f[i - 1] + temp

        return f[-1]

if __name__ == '__main__':
    #num = 26
    num = 12258
    print( Solution().translateNum(num) )