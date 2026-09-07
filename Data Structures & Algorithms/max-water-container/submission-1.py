class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            maxA = max(maxA, (r - l) * min(heights[r], heights[l]))
            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        return maxA


