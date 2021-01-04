class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if not n:
            return 0

        f = [ [0 for i in range(2)] for j in range(n+1) ]
        for i in range(1, n + 1):
            f[i][0] = max(f[i-1][1], f[i-1][0])
            f[i][1] = f[i-1][0] + nums[i-1]

        return max(f[-1])


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    nums = [2,7,9,3,1]
    print(Solution().rob(nums))