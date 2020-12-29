class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i -1]:
                f[i] = f[i-1] + 1

        return max(f)

# rolling nums
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        old,new = 1,1
        max_num = 1
        for i in range(1, len(nums)):

            if nums[i] > nums[i -1]:
                old = new
                new = old + 1
                max_num = max(new, max_num)
            else:
                new = 1

        return max_num

#how print Longest continuous increasing subsequence
#pi[] 初始化0，对于满足条件的序列进行标识。 找出时，仅需要比较标记段的长度


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    print(Solution().findLengthOfLCIS(nums))