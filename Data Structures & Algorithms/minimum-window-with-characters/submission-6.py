class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count = {}
        for char in t:
            count[char] = 1 + count.get(char, 0)
        win = {}
        have = 0
        need = len(count)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            char = s[r]
            win[char] = 1 + win.get(char, 0)
            if char in count and win[char] == count[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                win[s[l]] -= 1
                if s[l] in count and win[s[l]] < count[s[l]]:
                    have -= 1
                l +=1 
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                    

        