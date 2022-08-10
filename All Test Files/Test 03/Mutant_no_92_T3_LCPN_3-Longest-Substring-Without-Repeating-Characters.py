class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove( )
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

print(Solution.lengthOfLongestSubstring(s = "pwwkew"))