class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        charSet = set(s)
        for c in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                best = max(best, r - l + 1)
        return best


        