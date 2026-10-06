class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0
        leftM, rightM = height[l], height[r]
        while l < r:
            if leftM < rightM:
                l += 1
                leftM = max(leftM, height[l])
                total += leftM - height[l]
            else:
                r -= 1
                rightM = max(rightM, height[r])
                total += rightM - height[r]
        return total



        