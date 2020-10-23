import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for ele in nums:
            if len(heap) < k:
                heapq.heappush(heap, ele)
            else:
                heapq.heappush(heap, ele)
                heapq.heappop(heap)

        return heapq.heappop(heap)

# 10.23
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        k = len(nums) - k
        right = len(nums) - 1
        left = 0

        while left < right:
            partition_index = self.partition(nums, left, right)
            if partition_index == k:
                return nums[k]
            if partition_index < k:
                left = partition_index + 1
            else:
                right = partition_index - 1

        return nums[left]

    def partition(self, nums, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if nums[i] < nums[pivot]:
                self.switch(nums, i , index)
                index += 1
            i += 1

        self.switch(nums, pivot, index - 1)
        return index - 1

    def switch(self, nums, a, b):
        nums[a],nums[b] = nums[b],nums[a]

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for ele in nums:
            heapq.heappush(heap,-ele)
        temp = None
        while k:
            temp = heapq.heappop(heap)
            temp = -temp
            k -= 1
        return temp


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    #nums = [3,2,1,5,6,4]
    #nums = [-1, 2, 0]
    #k = 4
    nums = [99, 99]
    k = 1
    print( Solution().findKthLargest(nums, k)  )
