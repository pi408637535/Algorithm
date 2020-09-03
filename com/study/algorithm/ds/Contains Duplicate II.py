# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 12:03
# @Author  : piguanghua
# @FileName: Contains Duplicate II.py
# @Software: PyCharm


class Solution(object):

    def helper(self, slice):
        data_dict = {}
        for ele in slice:
            if not data_dict.get(ele):
                data_dict[ele] = True
            else:
                return False
        return True


    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = k + 1
        nums_rang = len(nums) - k + 1 if len(nums) - k + 1 > 0 else len(nums)
        for i in range(0, nums_rang):
            result = self.helper(nums[i:i+k])
            if result == False:
                return True

        return False

class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        data_dict = {}
        for index,ele in enumerate(nums):
            if data_dict.get(ele) == None:
                data_dict[ele] = index
            else:
                if index - data_dict[ele] <= k:
                    return True
                else:
                    data_dict[ele] = index
        return False
if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    print( Solution().containsNearbyDuplicate(nums,k))