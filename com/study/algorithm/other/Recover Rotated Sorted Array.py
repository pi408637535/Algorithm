class Solution:

    def recover(self, data, start, end):
        i = start
        j = end
        while i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
            i += 1
            j -= 1


    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        length = len(nums)
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                break

        if i == length - 2:
            return nums

        start = 0
        end = i
        self.recover(nums, start, end)
        self.recover(nums, end+1, length - 1)
        self.recover(nums, 0, length - 1)
        return nums


if __name__ == '__main__':
    data = [4, 5, 1, 2, 3]
    print( Solution().recoverRotatedSortedArray(data) )