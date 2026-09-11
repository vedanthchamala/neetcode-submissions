class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = []
        for char in s:
            if char.isalnum():
                new_str.append(char.lower())
        new = "".join(new_str)
        return new == new[::-1]

        