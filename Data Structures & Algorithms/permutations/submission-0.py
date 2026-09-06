class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, rem):
            if not rem:
                res.append(curr)
                return
            for i in range(len(rem)):
                c = curr.copy()
                r = rem.copy()
                c.append(rem[i])
                r.pop(i)
                dfs(c, r)
        
        dfs([], nums)
                
        return res