class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        maxFreq = 0
        for i in nums:
            freqs[i] += 1
            if freqs[i] > maxFreq:
                maxFreq = freqs[i]
        counts = [[] for i in range(maxFreq + 1)]
        for n, c in freqs.items():
            counts[c].append(n)
        
        ret = []
        for i in range(maxFreq):
            if k <= 0:
                break
            ret.extend(counts[maxFreq - i])
            k -= len(counts[maxFreq - i])
        
        return ret