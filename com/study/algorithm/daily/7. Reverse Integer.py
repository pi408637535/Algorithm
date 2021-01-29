class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = -1 if x < 0 else 1
        x = flag * x
        while x != 0:
            tmp = x % 10 * flag

            if res>214748364 or (res == 214748364 and tmp>7):
                return 0
            elif res<-214748364 or (res==-214748364 and tmp<-8):
                return 0
            else:
                x = x // 10

                res = res * 10 + tmp


        return res