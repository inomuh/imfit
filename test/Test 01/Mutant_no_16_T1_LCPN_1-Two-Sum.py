class Solution:
    def twoSum(nums, target):
        prevMap = {}  # val -> index

        while True:
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


print(Solution.twoSum(nums = [2,7,11,15], target= 9))