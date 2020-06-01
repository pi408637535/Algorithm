# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 16:16
# @Author  : piguanghua
# @FileName: binary_search.py
# @Software: PyCharm

#titile:binary-search
#Number:704

class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end: # 邻近or相等跳出循环
            mid = int( ( start + end) / 2 )
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if start + 1 == end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1

        elif nums[start] == target:
            return start
        else:
            return -1



if __name__ == '__main__':
    print(Solution().search([-1,0,3,5,9,12], 2))