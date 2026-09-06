class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        start = 0
        end = 0
        freq1 = [0] * 26 # 26 length list, each position corresponds to number of occurences
        # of that letter in alphabet
        for c in s1:
            freq1[ord(c) - ord('a')] += 1
        
        currRem = freq1[:] # create copy of frequences to store how many more times we need that letter
        while end < len(s2):
            if currRem[ord(s2[end]) - ord('a')] > 0: # we are on the right track
                currRem[ord(s2[end]) - ord('a')] -= 1 # update count of remaining characters
                if end - start + 1 == len(s1): # could we have redundancies still? no because at some point one of the remaining counts would be negative otherwise, which isn't possible
                    return True
            else: # we found a mistake
                # if the letter we found wasn't in the original word we restart at the next char
                if freq1[ord(s2[end]) - ord('a')] <= 0: # not in original word
                    start = end + 1
                    # we have to reset remaining characters
                    currRem = freq1[:]
                else: # we have one or more redundant characters in our current window
                    # can we have more than one redundant characters?
                    # i don't think so, this should trigger on the first redundancy
                    while s2[start] != s2[end]:
                        currRem[ord(s2[start]) - ord('a')] += 1
                        start += 1
                    start += 1
            end += 1
        return False