
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1

        heap = []

        for key in dic.keys():
            heapq.heappush(heap,  (-dic[key], key))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

if __name__ == '__main__':
    nums = ['1', '1', '1', '2', '2', '3']
    k = 2

    print(Solution().topKFrequent(nums, k))
