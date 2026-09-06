class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for i in nums:
            freqs[i] += 1
        return sorted(freqs.keys(), key = lambda x: -freqs[x])[:k]