class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            ret = [0] * 26
            word = word.lower()
            for l in word:
                ret[ord(l) - ord('a')] += 1
            d[tuple(ret)].append(word)
        
        return list(d.values())