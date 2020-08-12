# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 11:15
# @Author  : piguanghua
# @FileName: 剑指 Offer 56 - II. 数组中数字出现的次数 II.py
# @Software: PyCharm


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1

        num = 0
        for key,value in dic.items():
            if value == 1:
                num = key
                break


        return num

if __name__ == '__main__':
    nums = [3,4,3,3]
    print(Solution().singleNumber(nums))