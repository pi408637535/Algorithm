class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_queue1 = []
        index = 0
        for i,ele in enumerate(pattern):
            if i == 0:
                pattern_queue1.append(1)
            else:
                if ele == pattern[index]:
                    pattern_queue1[index] += 1
                else:
                    pattern_queue1.append(1)
                    index += 1

        index = 0
        pattern_queue2 = []
        for i, ele in enumerate(s.split(" ")):
            if i == 0:
                pattern_queue2.append(1)
            else:
                if ele == s.split(" ")[index]:
                    pattern_queue2[index] += 1
                else:
                    pattern_queue2.append(1)
                    index += 1

        i,j = 0, 0
        while i < len(pattern_queue1) and j < len(pattern_queue2):
            if pattern_queue1[i] == pattern_queue2[j]:
                i += 1
                j += 1
            else:
                return False
        if i == j:
            return  True
        else:
            return True


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        bijection = {}
        if len(pattern) != len(s.split(" ")):
            return False
        else:
            for ele in zip(pattern[::1], s.split(" ")):
                if not bijection.get(ele[0], None):
                    bijection[ele[0]] = ele[1]
                else:
                    if bijection[ele[0]] != ele[1]:
                        return False

        bijection = {}
        if len(pattern) != len(s.split(" ")):
            return False
        else:
            for ele in zip(pattern[::1], s.split(" ")):
                if not bijection.get(ele[1], None):
                    bijection[ele[1]] = ele[0]
                else:
                    if bijection[ele[1]] != ele[0]:
                        return False


        return True

if __name__ == '__main__':

    pattern = "abba"
    s = "dog dog dog dog"

    print(Solution().wordPattern(pattern, s))