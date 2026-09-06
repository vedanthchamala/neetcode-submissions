class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}
        for charS, charT in zip(s, t):
            freqS[charS] = 1 + freqS.get(charS, 0)
            freqT[charT] = 1 + freqT.get(charT, 0)
        if freqS != freqT:
            return False
        return True
        
        