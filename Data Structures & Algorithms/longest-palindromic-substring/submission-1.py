class Solution:
    def longestPalindrome(self, s: str) -> str:
        splitter = [''] * (2 * len(s))
        for i in range(len(s)):
            splitter[i * 2] = '#'
            splitter[i * 2 + 1] = s[i]
        splitter.append('#')
        s2 = ''.join(splitter)
        
        maxIdx = 0
        dp = [-1] * (2 * len(s) + 1)

        for i in range(len(s2)):
            # curr dp is center
            c = dp[i]
            if c < 0: # no palindrome reaches, use normal formula
                start = end = i
            else:
                # check mirror
                # set curr len to max mirror range and palindrome range
                # start checking for palindromes from there
                # set each of the next ones to the center if uninitialized
                cr = dp[c]
                m = c - (i - c)
                mr = dp[m]
                ir = min(cr - (c - m), mr)
                start = i - ir
                end = i + ir
            while start >= 0 and end < len(s2) and s2[start] == s2[end]:
                dp[end] = i
                start -= 1
                end += 1
            dp[i] = i - start
            if dp[i] > dp[maxIdx]:
                maxIdx = i
            
        res = ""
        for i in range(maxIdx - dp[maxIdx] + 1, maxIdx + dp[maxIdx]):
            if s2[i] != '#':
                res += s2[i]
        
        return res
