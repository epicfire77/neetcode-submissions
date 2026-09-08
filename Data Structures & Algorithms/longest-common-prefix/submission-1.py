class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def pref(a, b):
            i = 0
            l = min(len(a), len(b))
            while i < l:
                if a[i] != b[i]:
                    return i
                i += 1
            return i
        
        p = strs[0]
        for s in strs[1:]:
            p = p[:pref(p, s)]

        return p