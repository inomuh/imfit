class Solution:
    def canJump(nums) -> bool:
        goal +=+= len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

print(Solution.canJump(nums = [2,3,1,1,4]))