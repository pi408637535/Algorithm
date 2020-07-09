class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length1 = len(nums1) - 1


        i = m - 1
        j = n - 1

        if n == 0:
            return nums2

        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[length1] = nums1[i]
                i -= 1
                length1 -= 1

            else:
                nums1[length1] = nums2[j]
                j -= 1
                length1 -= 1

        #only a few tip..
        if i < 0:
            nums1[0:length1+1] = nums2[:j+1]





        return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1

    nums1 = [0]
    m = 1
    nums2 = [1]
    n = 1

    print( Solution().merge(nums1, m, nums2, n) )
