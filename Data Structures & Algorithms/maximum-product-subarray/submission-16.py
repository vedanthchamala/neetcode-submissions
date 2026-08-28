class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        


        maxi, mini = 1, 1
        res = nums[0]
        for num in nums:
            temp = maxi
            maxi = max(maxi * num, mini * num, num)
            mini = min(mini * num, temp * num, num)
            res = max(maxi, res)
        return res
        