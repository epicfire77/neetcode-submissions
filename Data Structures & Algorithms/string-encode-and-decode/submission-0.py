class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + ',' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            l = int(s[:s.find(',')])
            strs.append(s[s.find(',') + 1: s.find(',') + l + 1])
            s = s[s.find(',') + l + 1:]
        return strs