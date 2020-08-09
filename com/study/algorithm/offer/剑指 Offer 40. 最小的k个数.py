
import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        for ele in arr:
            heapq.heappush(heap, ele)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap) )
        return result



if __name__ == '__main__':
    arr = [3,2,1]
    k = 2

    print( Solution().getLeastNumbers(arr, k) )