class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in "+-/*":
                if len(stack) >= 2:
                    second = int(stack.pop())
                    first = int(stack.pop())
                    if tok == "+":
                        stack.append(first + second)
                    elif tok == "-":
                        stack.append(first - second)
                    elif tok == "*":
                        stack.append(first * second)
                    elif tok == "/":
                        stack.append(first / second)
            else:
                stack.append(tok)
        return int(stack[-1])
                    
                
        