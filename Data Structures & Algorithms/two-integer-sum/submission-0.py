class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in c:
                return [c[n], i]
            else:
                c[target - n] = i
