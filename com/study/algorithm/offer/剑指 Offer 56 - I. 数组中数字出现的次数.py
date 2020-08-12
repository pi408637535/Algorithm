# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 10:53
# @Author  : piguanghua
# @FileName: 剑指 Offer 56 - I. 数组中数字出现的次数.py
# @Software: PyCharm


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for ele in nums:
            res = res ^ ele
        div = 1
        while div & res == 0:
            div = div << 1

        a = 0
        b = 0
        for ele in nums:
            if ele & div == 0:
                a = ele ^ a
            else:
                b = ele ^ b

        return [a, b]


if __name__ == '__main__':
    nums = [3,2,1,3]
    print( Solution().singleNumbers(nums) )
