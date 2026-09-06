class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        op = ["{", "[", "("]
        cl = ["}", "]", ")"]
        for c in s:
            if c in op:
                d.append(c)
            elif c in cl:
                if not d:
                    return False
                o = d.pop()
                if o != op[cl.index(c)]:
                    return False
        return not d
                