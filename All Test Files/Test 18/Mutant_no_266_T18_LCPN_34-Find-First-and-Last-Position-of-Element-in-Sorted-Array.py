class Solution:
    def searchRange(nums, target: int):
        left = Solution.binSearch(nums, target, True)
        right = Solution.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return returni

print(Solution.searchRange(nums = [5,7,7,8,8,10], target = 8))