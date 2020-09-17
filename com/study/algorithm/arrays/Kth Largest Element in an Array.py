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



if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    #nums = [3,2,1,5,6,4]
    #nums = [-1, 2, 0]
    #k = 4
    nums = [99, 99]
    k = 1
    print( Solution().findKthLargest(nums, k)  )
