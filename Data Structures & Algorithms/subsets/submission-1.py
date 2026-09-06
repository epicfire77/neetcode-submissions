class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            a = [n]
            for i in range(len(res)):
                res.append(res[i] + a)
        return res