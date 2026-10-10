class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        mp = {}
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            best = max((r - l + 1), best)
        return best
        

        