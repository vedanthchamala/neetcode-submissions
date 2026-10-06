class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r, r_l = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            l_r[i] = l_r[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, - 1, - 1):
            r_l[i] = r_l[i + 1] * nums[i + 1]
        res = []
        for i in range(len(l_r)):
            res.append(l_r[i] * r_l[i])
        return res

        