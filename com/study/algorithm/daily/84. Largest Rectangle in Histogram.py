class Solution:
    def largestRectangleArea(self, heights):

        if not heights:
            return 0

        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] > heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = []
        for i in range(n-1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] > heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        max_num = -1
        for index,ele in enumerate(zip(left, right)):
            width = ele[1] - ele[0] - 1
            max_num = max(max_num, width * heights[index])

        return max_num


# class Solution:
#     def largestRectangleArea(self, heights) -> int:
#         n = len(heights)
#         left, right = [0] * n, [0] * n
#
#         mono_stack = list()
#         for i in range(n):
#             while mono_stack and heights[mono_stack[-1]] >= heights[i]:
#                 mono_stack.pop()
#             left[i] = mono_stack[-1] if mono_stack else -1
#             mono_stack.append(i)
#
#         mono_stack = list()
#         for i in range(n - 1, -1, -1):
#             while mono_stack and heights[mono_stack[-1]] >= heights[i]:
#                 mono_stack.pop()
#             right[i] = mono_stack[-1] if mono_stack else n
#             mono_stack.append(i)
#
#         ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
#         return ans



if __name__ == '__main__':
    heights = [4,1,3,2]
    heights = [2,1,5,6,2,3]
    heights = [1,1]
    print(Solution().largestRectangleArea(heights))
