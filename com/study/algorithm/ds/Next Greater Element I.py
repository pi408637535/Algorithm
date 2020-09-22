class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for index,ele in enumerate(nums2):
            dic[ele] = index
        ans = []
        for ele in nums1:
            index_second = dic[ele]


            while index_second < len(nums2):
                if ele < nums2[index_second]:
                    res = nums2[index_second]
                    break
                index_second += 1
            if index_second == len(nums2):
                res = -1
            ans.append(res)

        return  ans


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = []
        for ele in nums2:
            if not stack:
                stack.append(ele)
            while stack and ele > stack[-1]:
                dic[stack[-1]] = ele
                stack.pop()
            
            stack.append(ele)

        ans = []
        for ele in nums1:
            if not dic.get(ele):
                ans.append(-1)
            else:
                ans.append(dic.get(ele))

        return ans

if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    # nums1 = [2,4]
    # nums2 = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))