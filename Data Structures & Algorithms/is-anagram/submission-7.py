class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.charCount(s) == self.charCount(t)
        
        
    
    def charCount(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
        