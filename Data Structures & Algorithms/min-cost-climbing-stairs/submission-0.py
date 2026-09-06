class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            print(dp)
        
        return dp[-1]
        # [0, 0, 0, 0]
        # 2: min(0 + cost[1] = 0 + 2 = 2, 0 + cost[0] = 0 + 1 = 1) = 1
        # [0, 0, 1, 0]
        # 3: min(1 + cost[2] = 1 + 3 = 4, 0 + cost[1] = 0 + 2 = 2) = 2