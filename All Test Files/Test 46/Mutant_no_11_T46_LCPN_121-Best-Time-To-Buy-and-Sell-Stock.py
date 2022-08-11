class Solution:
    def maxProfit(prices) -> int:
        res = 0

        l = 0
        for r range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

print(Solution.maxProfit(prices = [7,1,5,3,6,4]))