class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        other = []
        for i in nums:
            if (i in other):
                return True
            else:
                other.append(i)
        return False