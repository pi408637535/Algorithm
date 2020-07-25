
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        return nums

if __name__ == '__main__':
    nums = [5,2,3,1]
    print(  Solution().sortArray(nums))