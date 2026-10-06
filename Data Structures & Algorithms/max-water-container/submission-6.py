class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            limit = min(heights[r], heights[l]) 
            curArea = limit * (r - l)
            best = max(best, curArea)
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1
        return best

        