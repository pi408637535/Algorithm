
'''
因为是仅返回一个Peak Element就行.
所以，仅需要在不断上升的波浪，挑选最可能找到那段就行。
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #最少有三个元素

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1


        start = 0
        end = len(nums) -1

        while start + 1 < end: #相等或相邻
            mid = int( (start + end) / 2 )
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid

        if start+1 == end and start == 0:
            if nums[0] > nums[end]:
                return 0
        elif end + 1 == len(nums):
            if nums[end] > nums[end-1]:
                return end

if __name__ == '__main__':
    print(Solution().findPeakElement([1,2,3]))