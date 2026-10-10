class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count = {}
        window = {}
        for char in t:
            count[char] = 1 + count.get(char, 0)
        have = 0
        need = len(count)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            char = s[r] 
            window[char] = 1 + window.get(char, 0)

            if char in count and window[char] == count[char]:
                have += 1 
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""





        
        

        