class Solution:
    def search(nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                elif:
                    r = mid - 1
            # right sorted portion
            elif:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                elif:
                    l = mid + 1
        return -1

print(Solution.search(nums = [4,5,6,7,0,1,2], target = 3))