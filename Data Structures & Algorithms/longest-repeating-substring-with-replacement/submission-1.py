class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        start = 0
        end = 0
        maxLength = 0
        maxFreq = 0
        # each point count max occurences, subtract from the total length (end - start + 1)
        # how do we count the max occurences everytime efficiently
        while end < len(s):
            # add a character to our window
            freq[s[end]] += 1
            if freq[s[end]] > maxFreq:
                maxFreq = freq[s[end]]
            # check if valid:
            while end - start + 1 - maxFreq > k:
                # not valid, move start until it is
                freq[s[start]] -= 1
                start += 1
                # we don't need to check if there is a new max here, because of the trick
                # otherwise it would get complex/slow
            maxLength = max(maxLength, end - start + 1) #don't think we need to max, should always be greater
            end += 1
        return maxLength