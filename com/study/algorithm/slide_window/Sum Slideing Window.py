# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 16:42
# @Author  : piguanghua
# @FileName: Sum Slideing Window.py
# @Software: PyCharm


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    ans = []
    for i in range(len(nums) - k + 1):
        value = sum(nums[i: i+k] )
        ans.append(value)
    print(ans)
