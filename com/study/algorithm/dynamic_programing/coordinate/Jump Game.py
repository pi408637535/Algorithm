class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        f = [False] * len(nums)
        f[0] = True

        for i in range(1, len(nums)):
            res = False
            for j in range(i,-1,-1):
                if f[j] == True and j + nums[j] >= i:
                    res = True
                    break
            f[i] = res

        return f[-1]


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump(nums))