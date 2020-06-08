# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:19
# @Author  : piguanghua
# @FileName: Search_in_Rotated_Sorted_Array.py
# @Software: PyCharm

#两个问题：1.是否是正常段 2.target是否在里面

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int( (start + end) / 2)
            if nums[mid] == target:
                return mid
            else:
                if nums[start] < nums[mid]: #norm
                    if nums[start] <= target and target <= nums[mid]:
                        end = mid
                    else:
                        start = mid
                else: #unnormal
                    if nums[mid] <= target and target <= nums[end]:
                        start = mid
                    else:
                        end = mid

        if start + 1 ==  end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
        else: #start == end
            if nums[end] == target:
                return  end

        return -1

if __name__ == '__main__':
    print( Solution().search([5,1,3], 3) )