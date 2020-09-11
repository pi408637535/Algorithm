import sys

class Solution(object):

    def helper(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1  + k - 1]

        if k == 1:
            return min(nums1[start1], nums2[start2])

        A_key = (nums1[start1 + k // 2 - 1]) if start1 + k // 2 - 1 < len(nums1) else sys.maxsize
        B_key = (nums2[start2 + k // 2 - 1]) if start2 + k // 2 - 1 < len(nums2) else sys.maxsize



        if A_key < B_key:
            return self.helper(nums1, start1 + k // 2, nums2, start2,  k - k // 2)
        else:
            return self.helper(nums1, start1, nums2, start2 + k // 2, k - k // 2)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k % 2 == 0:
            return (self.helper(nums1, 0, nums2, 0, k // 2) + \
                   self.helper(nums1, 0, nums2, 0, k // 2 + 1 )) / 2
        else:
            return self.helper(nums1, 0, nums2, 0, k // 2 + 1)



if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2,4]

    print( Solution().findMedianSortedArrays(nums1, nums2) )