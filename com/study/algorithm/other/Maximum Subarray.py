import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        sum = 0
        min_sum = 0
        max_sum = -sys.maxsize
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = max([max_sum,  sum - min_sum])
            min_sum = min([sum, min_sum ])

        return max_sum
        

if __name__ == '__main__':
    inputs = [-2,1,-3,4,-1,2,1,-5,4]
    print( Solution().maxSubArray(inputs) )