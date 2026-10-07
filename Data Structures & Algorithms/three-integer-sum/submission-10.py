class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l = 0
            l, r = i + 1, len(nums) - 1
            while l < r:
                three = nums[l] + nums[r] + a
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], a])
                    r -= 1 
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                
        