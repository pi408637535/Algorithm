class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        if len(nums) == 1:
            return nums[0]



        left = 0
        right = len(nums) - 1
        nums = self.quickSort(nums, left, right, right - k)

        if nums[-k] == nums[-k+1]:
            while nums[-k] == nums[-k+1]:
                if k == 0:
                    break
                k -= 1

        return nums[-k]




    def quickSort(self, nums, left, right, k):

        if left < right:
            partition_index = self.partition(nums, left, right)
            if partition_index > k:
               self.quickSort(nums, left, partition_index - 1, k)
            else:
                self.quickSort(nums, partition_index + 1, right, k)
        return nums

    def partition(self, nums, left, right):
        pivot = right
        index = pivot - 1
        i = index
        while left <= i:
            if nums[i] > nums[pivot]:
                self.swap(nums, i, index)
                index -= 1
            i -= 1

        self.swap(nums, pivot, index + 1)
        return index + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    #nums = [3,2,1,5,6,4]
    #nums = [-1, 2, 0]
    #k = 4
    nums = [99, 99]
    k = 1
    print( Solution().findKthLargest(nums, k)  )
