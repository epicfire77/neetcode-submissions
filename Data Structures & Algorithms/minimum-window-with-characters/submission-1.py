class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        needed = dict(freq)
        redund = {}
        start = 0
        end = 0
        res = ""
        # always try to move start up dispensible characters
        while end < len(s):
            if s[end] in needed:
                needed[s[end]] -= 1
                if needed[s[end]] == 0:
                    del needed[s[end]]
                    redund[s[end]] = 0
            elif s[end] in redund:
                redund[s[end]] += 1
            while start < end and s[start] not in needed and (s[start] not in redund or redund[s[start]] > 0):
                if s[start] in redund:
                    redund[s[start]] -= 1
                start += 1
            if not needed and not res or end - start + 1 < len(res):
                res = s[start : end + 1] 

            end += 1
            # need a way to check that we are done
        return res