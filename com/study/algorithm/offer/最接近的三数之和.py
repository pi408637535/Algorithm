class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = []
        min_diff = float('inf')
        for index, ele in enumerate(nums):

            left = index + 1
            right = len(nums) - 1

            while left < right:

                s = nums[left] + nums[right] + ele
                if abs(s - target) < min_diff:
                    res = sum([nums[left],nums[right],ele])
                    min_diff = abs(s - target)

                if s > target:
                    right -= 1
                else:
                    left += 1

        return res
if __name__ == '__main__':
    nums = [-1, 2, 1, -4];target = 1
    print(Solution().threeSumClosest(nums, target))