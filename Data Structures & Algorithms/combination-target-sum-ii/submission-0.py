class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # can either dfs with it or without it
        # can only be used as many times as it is in the array
        res = []
        candidates.sort()
        def dfs(i, curr, rem, skip):
            if rem == 0:
                res.append(curr)
                return
            if i >= len(candidates) or rem < 0:
                return
            if candidates[i] in skip:
                dfs(i + 1, curr, rem, skip)
                return
            sc = skip.copy()
            sc.add(candidates[i])
            dfs(i + 1, curr, rem, sc)
            sc.remove(candidates[i])
            cc = curr.copy()
            cc.append(candidates[i])
            dfs(i + 1, cc, rem - candidates[i], sc)
        
        dfs(0, [], target, set())

        return res
