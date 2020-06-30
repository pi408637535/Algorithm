class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [1 for i in range(len(nums))  ]
        #f[0] = 1

        for i in range(len(nums)):
            if i == 0: continue

            if nums[i] > nums[i - 1]:
                f[i] = f[i-1] + 1


        return max(f)


class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [1 for i in range(len(nums))  ]
        #f[0] = 1

        for i in range(len(nums)):
            if i == 0: continue

            for j in range(i):

                if nums[i] > nums[i - 1]:

                    f[i] = max([ f[j] + 1, f[i] ])


        return max(f)


class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [1 for i in range(len(nums))  ]
        #f[0] = 1

        for i in range(len(nums)):
            if i == 0: continue

            if nums[i] > nums[i - 1]:
                for j in range(i):



                    f[i] = max([ f[j-1] + 1, f[i] ])


        return max(f)

if __name__ == '__main__':
    input =  [10,9,2,5,3,7,101,18]
    #input = [4,10,4,3,8,9]
    print( Solution().lengthOfLIS(input) )