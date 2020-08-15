class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        b = [1 for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a)):
                if j != i:
                    b[j] *= a[i]
        return b

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """

        if len(a) == 0:
            return 0

        f1 = [1]

        for i in range(1, len(a)):
            f1.append(a[i-1] * f1[i - 1])

        f2 = [1 for i in range(len(a))]
        f2[len(a) - 1] = 1
        for i in range(len(a)-2, -1, -1):
            f2[i] = a[i+1] * f2[i+1]

        b = []
        for i in range(len(a)):
            b.append( f1[i] * f2[i] )

        return b

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print( Solution().constructArr(nums) )