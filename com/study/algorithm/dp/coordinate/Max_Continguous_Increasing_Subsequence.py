class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        max_length = 1
        length = len(nums)

        if length == 0:
            return 0

        f = [ [0 for j in range(2) ] for i in range(length) ]

        for i in range(length):
            f[i][0] = 1

        for i in range(length):
            if i == 0: continue
            if nums[i] > nums[i - 1]:
                f[i][0] += f[i-1][0]
                if f[i][0] > max_length:
                    f[i][1] = f[i][0]
                    max_length = f[i][0]

        return max_length


if __name__ == '__main__':
    #data = [1,3,5,4,7]
    #data = [2,2,2,2,2]
    data = [1, 3, 5, 4, 7, 8, 9,10]
    print( Solution().findLengthOfLCIS(data) )