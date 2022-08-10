class Solution:
    def climbStairs(n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

         
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

print(Solution.climbStairs(n=2))