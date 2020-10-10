class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i ,j = 0,0
        data_set = set()
        n = len(s)
        while i < n and j < n:
            if  s[j] not in data_set:
                data_set.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                data_set.remove(s[i])
                i += 1
        return ans

if __name__ == '__main__':
    #s = "abcabcbb"
    #s = "bbbbb"
    s = "pwwkew"
    #s = "a"
    #s = "aab"
    #s = 'abccbdddd'
    print(Solution().lengthOfLongestSubstring(s))


