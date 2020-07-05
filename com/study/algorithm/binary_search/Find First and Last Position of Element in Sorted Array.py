class Solution(object):

    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1

        if len(nums) == 0:
            return -1

        while start + 1 < end:
            mid = int( (start + end) / 2 )
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if start + 1 == end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return target
        else:
            if nums[end] == target:
                return target

        return -1

    def searchRange(self, nums, target):

        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid


    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1

        output = []


        while start + 1 < end:
            mid =int( (start  + end) / 2 )
            if nums[mid] == target:
                output.append(mid)
                if nums[mid+1] == target:
                    output.append(mid+1)
                    break
                elif nums[mid-1] == target:
                    output.append(mid-1)
                else:
                    start = mid
                break

            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if start + 1 == end:
            if nums[start] == target and nums[end] == target:
                return [start, end]
            elif nums[start] == target:
                return [start,start]
            elif nums[end] == target:
                return [end, end]
            else:
                return [-1, -1]


        if start == end:
            if nums[start] == target:
                return [start,start]
            else:
                return [-1,-1]

        if len(output) == 0:
            return [-1,-1]
        else:
            return output



if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]

    target = 6

    nums = [2,2]
    target = 2

    nums = [1,2,3]
    target = 2
    nums = [5,7,7,8,8,10]
    target = 8
    #nums = [1, 1, 2]
    #target = 1
    print( Solution().searchRange(nums, target) )