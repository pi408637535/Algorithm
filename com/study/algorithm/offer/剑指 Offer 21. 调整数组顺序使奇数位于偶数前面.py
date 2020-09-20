
#Todo 要优化
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data1 = []
        data2 = []
        for ele in nums:
            if ele % 2 == 0:
                data2.append(ele)
            else:
                data1.append(ele)
        return data1 + data2


class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) -1
        while left < right:
            while left < right and nums[left] % 2 != 0:
                #nums[left],nums[right] = nums[right],nums[left]
                left += 1

            while left < right and nums[right] % 2 == 0:
                #nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            if left < right and nums[left] % 2 == 0 and nums[right] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]

        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print( Solution().exchange(nums) )
