import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i in range(k):
            h.append([-nums[i], -i])
        heapq.heapify(h)
        res = [-h[0][0]]
        start = 0
        while start + k < len(nums): # need to check if k == len(nums)
            heapq.heappush(h, [-nums[start + k], -(start + k)]) # add newest element
            val, pos = h[0] # should be the max element currently in our heap
            while -pos <= start:
                heapq.heappop(h)
                val, pos = h[0] # should be the max element currently in our heap
            res.append(-val)
            start += 1
        
        return res