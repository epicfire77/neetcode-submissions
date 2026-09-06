class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bef = [1] * (n + 1)
        aft = [1] * (n + 1)
        for i in range(1, n + 1):
            bef[i] = bef[i - 1] * nums[i - 1]
            aft[-i - 1] = aft[-i] * nums[-i]
        ret = [1] * n
        for j in range(n):
            ret[j] = bef[j] * aft[j + 1]
        return ret