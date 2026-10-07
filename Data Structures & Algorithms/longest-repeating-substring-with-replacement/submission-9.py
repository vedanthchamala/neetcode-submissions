class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        best = 0
        for char in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                
                best = max(best, (r - l + 1))
        return best



        