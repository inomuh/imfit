class Solution:
    def climbStairs(n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

print(Solution.climbStairs(n=2))