class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        best = 0


        for num in nums:
            if (num - 1) not in numSet:
                cur = 1
                while (num + cur) in numSet:
                    cur += 1
                best = max(cur, best)
        return best
        