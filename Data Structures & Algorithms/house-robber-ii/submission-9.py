class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.rober(nums[1:]), self.rober(nums[:-1]))

    
    def rober(self, arr):
        rob1, rob2 = 0, 0

        for i in range(len(arr)):
            arr[i] = max(rob1 + arr[i], rob2)
            rob1, rob2 = rob2, arr[i]
        return rob2

        