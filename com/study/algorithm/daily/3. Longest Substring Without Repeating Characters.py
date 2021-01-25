
#dp
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        f = [1] * n
        for i in range(1, len(s)):
            if f[i - 1] != 1:
                data_set = s[i - f[i - 1] : i]
                if s[i] not in data_set:
                    f[i] = f[i- 1] + 1
                else:
                    temp = list(s[i - f[i - 1] : i])
                    while temp:
                        if s[i] in temp:
                            temp.pop(0)
                        else:
                            break
                    f[i] = len(temp) + 1

            else:
                if s[i] != s[i-1]:
                    f[i] = f[i-1] + 1

        return max(f)

if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "pwwkew"
    # s = "bbbbb"
    # s = " "
    s = "aucde"
    s = ""
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))