class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for i in range(len(nums)):
            if data.get(nums[i]) == None:
                data[nums[i]] = True
            else:
                return nums[i]


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print( Solution().findRepeatNumber(nums) )