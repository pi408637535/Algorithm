

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(1, n):
            pre_index = i -1
            current = nums[i]
            while pre_index >= 0 and current < nums[pre_index]:
                nums[pre_index+1] = nums[pre_index]
                pre_index -= 1
            nums[pre_index + 1] = current
        return nums

if __name__ == '__main__':
    nums = [5,2,3,1]
    print(  Solution().sortArray(nums))