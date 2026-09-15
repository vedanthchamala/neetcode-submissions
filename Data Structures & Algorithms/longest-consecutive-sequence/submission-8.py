class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        best = 0


        for num in nums:
            if (num - 1) not in numSet:
                cur = 1
                while (num + cur) in numSet:
                    cur += 1
                if cur > best:
                    best = cur
        return best
        