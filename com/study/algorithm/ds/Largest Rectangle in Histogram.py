class Solution(object):

    #获取index向左，向右，获取weight
    def helper(self, index, height, heights):
        weight = 1
        if index == 0:
            for ele in heights[1:]:
                if ele >= height and ele:
                    weight += 1
                else:
                    break
        elif index == len(heights) -1:
            for ele in heights[::-1][1:]:
                if ele >= height and ele:
                    weight += 1
                else:
                    break
        else:
            left = 0
            right = len(heights) - 1
            temp = index
            while left < index:
                if heights[index-1] >= height and heights[index-1]:
                    weight += 1
                else:
                    break
                index -= 1

            index = temp
            while index < right:
                if heights[index+1] >= height and heights[index-1]:
                    weight += 1
                else:
                    break
                index += 1

        return  weight


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        res = [0]
        for index,ele in enumerate(heights):
            if ele != 0:
                weight = self.helper(index, ele, heights)
                res.append(weight * ele)

        return max(res)

#stack
#相比brute method最大改进，将元素的索引放入stack中，优化了确定weight步骤
class Solution(object):


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights:
            return 0

        stack = []
        new_heights = []
        new_heights.append(0)
        new_heights.extend(heights)
        new_heights.append(0)
        max_num = 0

        for index,ele in enumerate(new_heights):

            while stack and new_heights[stack[-1]] > ele:
                top_ele = stack.pop()
                height = new_heights[top_ele]

                if not stack:
                    weight = index - top_ele
                else:
                    weight = index - stack[-1] -1 #重点在这里。stack[-1]代表左边界，index右边界

                max_num = max(height * weight, max_num)


            stack.append(index)

        return max_num


if __name__ == '__main__':

    #nums = [2,1,5,6,2,3]
    #nums = [0,1,0,1]
    #nums = []
    #nums = [0]
    nums = [2,1,2]

    print(Solution().largestRectangleArea(nums))