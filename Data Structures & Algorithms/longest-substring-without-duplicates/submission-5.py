class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        maxLength = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in pos and pos[c] >= start: #found a repeat
                maxLength = max(maxLength, i - start)
                start = pos[c] + 1 # start after previous position of the character
            pos[c] = i
        maxLength = max(maxLength, len(s) - start)
        return maxLength