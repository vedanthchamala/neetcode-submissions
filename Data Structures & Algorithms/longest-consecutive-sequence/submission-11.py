class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        best = 0

        for num in check:
            if (num - 1) not in check:
                rec = 1
                while (num + rec) in check:
                    rec += 1
                best = max(best, rec)
        return best

            

        