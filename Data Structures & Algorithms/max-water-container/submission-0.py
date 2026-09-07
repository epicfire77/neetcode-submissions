class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l, r):
            return (r - l) * min(heights[r], heights[l])
        maxA = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            maxA = max(maxA, area(l, r))
            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        return maxA


