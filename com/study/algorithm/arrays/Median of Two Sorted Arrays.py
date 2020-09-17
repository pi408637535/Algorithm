
#边界条件太难确定了

import sys

class Solution(object):
    #k是总共向前走的步伐
    def helper(self, num1, start1, num2, start2, k):

        if len(num1) <= start1:
            return num2[start2 + k - 1]

        if len(num2) <= start2:
            return num1[start1 + k - 1]

        if k == 1:
            return min(num1[start1], num2[start2])

        key_a = sys.maxsize if start1 + k // 2 - 1 > len(num1) else num1[start1 + k // 2 - 1]
        key_b = sys.maxsize if start2 + k // 2 - 1 > len(num2) else num2[start2 + k // 2 - 1]

        if key_a < key_b:
            return self.helper(num1, start1 + k // 2, num2, start2, k - k // 2)
        else:
            return self.helper(num1, start1, num2, start2 + k // 2, k - k // 2  )

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)

        if length % 2 == 0:
            return (self.helper(nums1, 0, nums2, 0, length // 2 + 1)+
                    self.helper(nums1, 0, nums2, 0, length // 2)) / 2
        else:
            return self.helper(nums1, 0, nums2, 0, length // 2 + 1)


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print( Solution().findMedianSortedArrays(nums1, nums2) )