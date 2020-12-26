class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left, right = [], []

        mono_stack = []
        for index,ele in enumerate(heights):
            while mono_stack and ele < mono_stack[-1][1]:
                mono_stack.pop()
            left.append( index - mono_stack[-1][0] if mono_stack else 0)
            mono_stack.append((index,ele))

        mono_stack = []
        for index,ele in enumerate(heights[::-1]):
            while mono_stack and ele < mono_stack[-1][1]:
                mono_stack.pop()
            right.append( index - mono_stack[-1][0] if mono_stack else 0)
            mono_stack.append((index,ele))

        max_num = -1
        for index,ele in enumerate(zip(left, right[::-1])):
            if ele[0] == ele[1] and ele[0] == 0 and ele[1] == 0:
                max_num = max(max_num, heights[index] * len(heights))
            elif ele[0] == ele[1] :
                max_num = max(max_num, heights[index] * 1 )
            else:
                max_num = max(max_num, heights[index] * abs(ele[0] - ele[1]))
        return max_num


class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans



if __name__ == '__main__':
    heights = [4,1,3,2]
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights))
