class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(T)

        for index,ele in enumerate(T):
            while stack and T[stack[-1]] < ele:
                ans[stack.pop()] = index - stack[-1]
            stack.append(index)

        return ans

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))
