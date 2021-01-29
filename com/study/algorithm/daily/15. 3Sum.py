class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        n = len(nums)
        #unique triplets
        #排序后，既然防止左边重复，也要防止右边重复
        '''
            防止左、右边重复：1. left+middle+right = 0时，右边重复要right -= 1,左边重复要 left += 1
                           2. 在left > 1时，确保 num[L-1],num[L] 不一样
        '''
        res = []
        for i,ele in enumerate(nums):

            if i >= 1 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                result = ele + nums[l] + nums[r]
                if result > 0:
                    r -= 1
                elif result < 0:
                    l += 1
                else:
                    res.append([ele, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1


        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0,0]

    print(Solution().threeSum(nums))