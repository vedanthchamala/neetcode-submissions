class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        goal = n - 1
        jumps = [float('inf')] * n
        jumps[n - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    jumps[i] = min(jumps[i], 1 + jumps[i + jump])
        return jumps[0]