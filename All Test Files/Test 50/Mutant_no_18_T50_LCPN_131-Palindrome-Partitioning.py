class Solution:
    def partition(s: str):
        res, part = [], []

        def dfs(i):
            if i   len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if Solution.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

print(Solution.partition(s = "aab"))