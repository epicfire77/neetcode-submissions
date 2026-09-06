class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            d = 0
            if i + 2 < len(nums):
                d = dp[i + 2]
            dp[i] = max(dp[i + 1], nums[i] + d)
        return dp[0]