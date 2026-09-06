class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return False
        need = {}
        for let in t:
            need[let] = need.get(let, 0) + 1
        cur_win = {}
        res, res_len = [-1, -1], float("inf")
        have, required = 0, len(need)
        l = 0
        for r in range(len(s)):
            char = s[r]
            cur_win[char] = cur_win.get(char, 0) + 1
            if char in need and cur_win[char] == need[char]:
                have += 1
            while have == required:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                cur_win[s[l]] -= 1
                if s[l] in need and cur_win[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]: res[1] + 1] if res_len != float("inf") else ""














            


        