class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
            思路: 设左边和为 sum, 总共和为 total。则右边和为 total - sum - num_i = 右边
            所以： total -sum - num_i = sum
        '''
        if not nums:
            return -1
        total = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i]) * 2 + nums[i] == total:
                return i
        return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    # nums = [-1,-1,-1,-1,-1,0]
    print(Solution().pivotIndex(nums))
