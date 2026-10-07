class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        best = 0
        mp = {}

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            best = max(best, (r - l + 1))
        return best






        