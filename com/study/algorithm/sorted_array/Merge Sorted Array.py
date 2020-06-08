# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 10:32
# @Author  : piguanghua
# @FileName: Merge Sorted Array.py
# @Software: PyCharm

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


        if n == 0:
            return

        i = 0
        j = 0

        num3 = [0] * (m + n)
        for k in range(m+n):

            if nums1[i] <= nums2[j]  and nums1[i] != 0:
                num3[k] = nums1[i]
                i += 1
            elif nums1[i] == 0:
                num3[k] = nums2[j]
                j += 1
            else:
                num3[k] = nums2[j]
                j += 1

            if j == n:
                break
        if j == n:
            if k != m+n - 1
            num3[k+j:] = nums1[i:k+1]


        for i in range(len(nums1)):
            nums1[i] = num3[i]



if __name__ == '__main__':
    num1 = [4,5,6,0,0,0]
    num2 = [1,2,3]
    Solution().merge(num1, 3, num2, 3)
    print(num1)
