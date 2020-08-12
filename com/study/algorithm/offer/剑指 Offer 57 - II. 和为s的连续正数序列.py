# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 17:01
# @Author  : piguanghua
# @FileName: 剑指 Offer 57 - II. 和为s的连续正数序列.py
# @Software: PyCharm

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = [i for i in range(1,target)]

        self.flag = False

        def slide_window(target, k):

            for i in range(len(nums) - k + 1):
                if sum(nums[i:k]) == target:
                    ans.append(nums[i:k])




        for k in range(2, target):
            slide_window(target, k)


        return ans

if __name__ == '__main__':
    target = 15
    print(Solution().findContinuousSequence(target))