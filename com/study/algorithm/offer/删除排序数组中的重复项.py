class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        slow,fast = 0,0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]


        return slow + 1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums) )
    print(nums)
