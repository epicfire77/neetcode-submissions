class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def nxt(i, nums):
            curr = nums[i]
            while i < len(nums) and nums[i] == curr:
                i += 1
            return i
        
        def twoSum(nums, n):
            s = set()
            ret = []
            i = 0
            while i < len(nums):
                j = nums[i]
                if -(n+j) in s:
                    ret.append([n, j, -(n+j)])
                    i = nxt(i, nums)
                else:
                    s.add(j)
                    i += 1
            return ret
        
        ret = []
        i = 0
        while i < len(nums) - 1:
            ret.extend(twoSum(nums[i + 1:], nums[i]))
            i = nxt(i, nums)
        
        return ret
