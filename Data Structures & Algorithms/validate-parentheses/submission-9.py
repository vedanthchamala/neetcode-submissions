class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for tok in s:
            if tok in mp:
                if stack and stack[-1] == mp[tok]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(tok)
        return True if not stack else False
            
        