class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(currCombo, remNums, currTarget):
            print(currCombo, remNums, currTarget)
            r = remNums[:]
            if currTarget == 0:
                res.append(currCombo)
            if currTarget < 0:
                return
            for n in remNums:
                r.pop(0)
                copy = currCombo[:]
                ct = currTarget
                while n <= ct:
                    ct -= n
                    print(n, ct)
                    copy.append(n)
                    dfs(copy, r, ct)

        dfs([], nums, target)

        return res