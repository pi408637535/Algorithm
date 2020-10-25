class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for ele in nums:
            ans ^= ele

        return ans

if __name__ == '__main__':
    nums = [2,2,1]
    print( Solution().singleNumber(nums) )