class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for index, ele in enumerate(nums):
            if index >= 1 and nums[index - 1] == nums[index]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:

                s = nums[right] + nums[left] + ele
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1

                else:
                    res.append([ele, nums[left], nums[right]])

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1

        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums))
