class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return list(nums1_set & nums2_set)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print(Solution().intersection(nums1, nums2))