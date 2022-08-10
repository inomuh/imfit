class Solution:
    def jump(nums) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            while True:
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

print(Solution.jump(nums = [2,3,1,1,4]))