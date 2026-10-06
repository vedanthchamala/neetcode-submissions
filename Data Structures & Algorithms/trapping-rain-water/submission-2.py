class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftM, rightM = height[l], height[r]
        total = 0
        while l < r:
            if leftM < rightM:
                l += 1
                leftM = max(height[l], leftM)
                total += leftM - height[l]
            else:
                r -= 1
                rightM = max(height[r], rightM)
                total += rightM - height[r]
        return total

        