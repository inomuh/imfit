class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max( )
        return res

print(Solution.lengthOfLongestSubstring(s = "pwwkew"))