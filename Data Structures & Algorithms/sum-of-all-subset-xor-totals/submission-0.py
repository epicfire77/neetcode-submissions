class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        subs = []
        for n in nums:
            for i in range(len(subs)):
                s = subs[i]
                subs.append(s^n)
            subs.append(n)
        res = sum(subs)
        return res
