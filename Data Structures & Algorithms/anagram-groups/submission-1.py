class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w = {}
        for i in strs:
            l = [0]*26
            for j in i:
                l[ord(j) - ord('a')] += 1
            if tuple(l) in w:
                w[tuple(l)].append(i)
            else:
                w[tuple(l)] = [i]
        return list(w.values())