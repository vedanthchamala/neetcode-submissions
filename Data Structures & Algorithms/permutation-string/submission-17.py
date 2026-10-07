class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        win = Counter(s2[:len(s1)])
        if win == need:
            return True
        for r in range(len(s1), len(s2)):
            win[s2[r]] += 1
            left = s2[r - len(s1)]
            win[left] -= 1
            if win[left] == 0:
                del win[left]
            if win == need:
                return True
        return False
        