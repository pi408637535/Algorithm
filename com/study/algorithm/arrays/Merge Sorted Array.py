class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1) - 1

        if n == 0:
            return m

        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[length] = nums1[m]
                m -= 1
            else:
                nums1[length] = nums2[n]
                n -= 1
            length -= 1


        if n < 0:
            return nums1
        else:
            nums1[:n+1] = nums2[:n+1]
            return nums1



if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print( Solution().merge(nums1, m, nums2, n) )