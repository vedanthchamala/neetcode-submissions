class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #basically just start from the beginning, stretch out until all the counts are met, and then while we have all the elements in our current window, check size, then shrink, then check size, and then shrink, and keep doing that until we can't, then the left pointer will be one past whenever our need and have isn't the same
        if t == "":
            return ""
        count, win = {}, {}
        for char in t:
            count[char] = 1 + count.get(char, 0)
        need = len(count)
        have = 0
        l = 0
        res = [-1, -1]
        resLen = float("infinity")
        for r in range(len(s)):
            char = s[r]
            win[char] = 1 + win.get(char, 0)
            if char in count and win[char] == count[char]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                win[s[l]] -= 1
                if s[l] in count and win[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


        