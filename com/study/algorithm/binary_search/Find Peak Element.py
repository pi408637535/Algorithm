class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            if nums[-1] > nums[-2]:
                return 1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid

        if nums[start] > nums[start -1] and nums[start] > nums[start +1]:
            return start
        elif nums[end] > nums[end -1] and nums[end] > nums[end +1]:
            return end
        else:
            return -1




if __name__ == '__main__':
    nums = [1,2,3]
    print( Solution().findPeakElement(nums) )