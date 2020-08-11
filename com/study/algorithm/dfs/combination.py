# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 09:07
# @Author  : piguanghua
# @FileName: combination.py
# @Software: PyCharm

nums = [1,2,3]
ans = []

def dfs(n, s, cur):
    if len(cur)  == n:
        ans.append(cur.copy())
        return

    for i in range(s, len(nums)):
        cur.append(nums[i])
        dfs(n, i + 1, cur)
        cur.pop()

if __name__ == '__main__':
    for i in range(len(nums)+1):
        dfs(i, 0, [])

    print(ans)