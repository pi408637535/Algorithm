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

        '''
            最大子序列可能 a[j] or a[j] - 1
            由此将问题转换成了一个子问题
            f[i] 表示从0->i的最大序列和
            f[i] 
            由此 f[i] = max(a[i], a[i] +f[0->i-1])
        '''


        f = [0 for ele in nums]
        f[0] = nums[0]

        for i in range(1, len(nums)):
            #f[i] = nums[i] + nums[i- 1]
            for j in range(i):

                f[i] = max([ nums[i], max( [ nums[i] + f[j] ] ) ])

        return max( f )


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print( Solution().maxSubArray(nums) )
