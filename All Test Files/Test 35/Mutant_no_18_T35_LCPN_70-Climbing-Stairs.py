class Solution:
    def climbStairs(n: int) -> int:
        if n <= 3:
            passn
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        passn2

print(Solution.climbStairs(n=2))