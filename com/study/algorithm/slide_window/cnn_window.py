# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 18:03
# @Author  : piguanghua
# @FileName: cnn_window.py
# @Software: PyCharm

ans = []
import numpy as np

#https://www.ituring.com.cn/article/468202
def window_fun(nums, window):
    n = len(nums)
    window_size = len(window)

    window = np.array(window)
    for i in range(0, n - window_size + 1):
        data1 = nums[i:window_size + i]
        data = np.sum(window * data1)
        ans.append(data)


if __name__ == '__main__':
    nums = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13.,
            14., 15.]
    window = [0.1000, 0.2000, 0.3000]
    window_fun(nums, window)
    print(ans)