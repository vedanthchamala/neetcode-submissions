class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []
        for char in s:
            if char.isalnum():
                newStr.append(char.lower())
        new = "".join(newStr)
        return new[::-1] == new

        