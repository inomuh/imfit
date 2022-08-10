class Solution:
    def permute(nums):
        res = []

        # base case
        if len(nums)  ====  1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = Solution.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

print(Solution.permute(nums = [1,2,3]))