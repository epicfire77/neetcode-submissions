class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHelp(ns):
            if len(ns) == 1:
                return [ns[0], ns[0]]
            dp = [0] * len(ns)
            dp[-1] = ns[-1]
            for i in range(len(ns) - 2, -1, -1):
                d = 0
                if i + 2 < len(ns):
                    d = dp[i + 2]
                dp[i] = max(dp[i + 1], ns[i] + d)
            return [dp[0], dp[1]]
        
        return max(robHelp(nums)[1], robHelp(nums[:-1])[0])
        
        