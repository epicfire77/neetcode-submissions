class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        longest = 0
        for n in nums:
            if n in d:
                continue
            
            d[n] = [n, n]
            before = False
            if n - 1 in d:
                before = True
                d[n][0] = d[n - 1][0]
                d[d[n - 1][0]][1] = n
            
            if n + 1 in d:
                d[n][1] = d[n + 1][1]
                d[d[n + 1][1]][0] = d[n][0]
                if before:
                    d[d[n - 1][0]][1] = d[n][1]
            
            longest = max(longest, d[n][1] - d[n][0] + 1)
        
        return longest
