class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 101
        maxProfit = 0
        for p in prices:
            if p > start:
                maxProfit = max(maxProfit, p - start)
            else:
                start = p
        return maxProfit