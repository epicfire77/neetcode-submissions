class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = {}
        for i in s:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        
        for j in t:
            if j in l:
                if l[j] <= 0:
                    return False
                l[j] -= 1
            else:
                return False
        
        for k, v in l.items():
            if v != 0:
                return False

        return True