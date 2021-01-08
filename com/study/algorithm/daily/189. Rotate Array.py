
#逐位移动，太慢了
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_nums = nums
        while k:
            new_nums = [new_nums[-1]] + new_nums[:-1]
            k -= 1
        for i in range(len(nums)):
            nums[i] = new_nums[i]
        # return nums

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        new_nums = nums[-k:] + nums[:n - k]
        for i in range(len(nums)):
            nums[i] = new_nums[i]

#reverse : global + local
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums) - 1
        self._reverse(nums, 0, n)
        k = k % len(nums)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, n)

    def _reverse(self, nums, s, e):
        while s < e:
            nums[s],nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

    # def _reverse(self, nums):
    #     n = len(nums)
    #     if not n:
    #         return
    #     for i in range(n // 2):
    #         nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]


if __name__ == '__main__':
    nums = [1,2,3,4]
    k = 2



    # nums = [-1,-100,3,99]
    # k = 2
    Solution().rotate(nums, k)
    print(nums)