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
            #mid = int( ( start + end) / 2 )
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


if __name__ == '__main__':
    nums, target = [1, 3, 5, 6], 7
    print(Solution().search(nums, target))