# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 13:06
# @Author  : piguanghua
# @FileName: 剑指 Offer 42. 连续子数组的最大和.py
# @Software: PyCharm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0] * len(nums)
        f[0] = nums[0]

        for i in range(1,len(nums)):
            f[i] = max(nums[i], f[i-1] + nums[i])

        return max(f)

class Solution(object):
    def maxSubArray(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      if not nums:
         return 0
      f = [0] * len(nums)
      f[0] = nums[0]
      for i in range(1, len(nums)):
            f[i] = max(nums[i], nums[i] + f[i - 1])

      return max(f)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print( Solution().maxSubArray(nums) )
