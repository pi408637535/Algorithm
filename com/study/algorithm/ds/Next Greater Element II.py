class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [-1] * len(nums)

        for index,ele in enumerate(nums):
            while stack and nums[stack[-1]] < ele:
                ans[stack.pop()] = ele
            stack.append(index)

        for index, ele in enumerate(nums):
            while stack and nums[stack[-1]] < ele:
                ans[stack.pop()] = ele

        return ans