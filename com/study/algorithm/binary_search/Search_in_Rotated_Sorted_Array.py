# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:19
# @Author  : piguanghua
# @FileName: Search_in_Rotated_Sorted_Array.py
# @Software: PyCharm

#两个问题：1.是否是正常段 2.target是否在里面
#https://www.jianshu.com/p/874e1d6a3156

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

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

# 10.23
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]: #normal
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

if __name__ == '__main__':
    print(Solution().search([5, 1, 3, 0], 0))



if __name__ == '__main__':
    print( Solution().search([5,1,3], 3) )