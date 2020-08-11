# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 09:19
# @Author  : piguanghua
# @FileName: permutation.py
# @Software: PyCharm


nums = [1,2,3]
ans = []
used = [False] * len(nums)

def dfs(n, cur):
    if len(cur) == n:
        ans.append(cur.copy())
        return
    for i in range(0, len(nums)):
        if used[i]: continue
        used[i] = True
        cur.append(nums[i])
        dfs(n, cur)
        cur.pop()
        used[i] = False

for i in range(0, len(nums)+1):
    dfs(i, [])

print(ans)