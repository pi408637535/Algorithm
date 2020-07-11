import math
import sys

#https://www.wxwenku.com/d/108911527

class Solution(object):
    def findKth(self, arrayA, arrayA_start, arrayB, arrayB_start, k):
        if arrayA_start > len(arrayA):  # arrayA has no element
            return arrayB[arrayB_start + k - 1]

        if arrayB_start > len(arrayB):
            return arrayA[arrayA_start + k - 1]

        if k == 1: # arrayA and arrayB have only one element
            return min( arrayA[arrayA_start],arrayB[arrayB_start] )

        #gain K/2 element
        #If we couldn't gain element, we gain sys.maxsize.
        A_key = arrayA[arrayA_start + int(k / 2) ] if arrayA_start + int(k / 2) < len(arrayA) else sys.maxsize
        B_key = arrayB[arrayB_start + int(k / 2) ] if arrayB_start + int(k / 2) < len(arrayB) else sys.maxsize

        if A_key < B_key:
            return self.findKth(arrayA, arrayA_start + int(k/2), arrayB, arrayB_start, k - int(k/2))
        else:
            return self.findKth(arrayA, arrayA_start, arrayB, arrayB_start + int(k / 2), k - int(k / 2))




    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return self.findKth(nums1, 0, nums2, 0, int(length / 2)) + self.findKth(nums1, 0, nums2, 0, int(length / 2) + 1)
        else:
            return self.findKth(nums1, 0, nums2, 0, int(length / 2))


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,5]
    print( Solution().findMedianSortedArrays(nums1,nums2) )