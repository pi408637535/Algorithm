# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 13:57
# @Author  : piguanghua
# @FileName: Contains Duplicate.py
# @Software: PyCharm

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = False
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if not flag:
                    if nums[j] == nums[i]:
                        flag = True
                        break

        return flag

if __name__ == '__main__':
    nums = [1,2,3,1]
    #nums = [3,3]
    print( Solution().containsDuplicate(nums) )