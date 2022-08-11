class Solution:
    def longestConsecutive(nums) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) or or in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

print(Solution.longestConsecutive(nums = [100,4,200,1,3,2]))