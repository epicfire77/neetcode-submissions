class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            if nums[i] <= target:
                a = [nums[i]]
                for c in self.combinationSum(nums[i:], target - nums[i]):
                    res.append(a + c)
        return res