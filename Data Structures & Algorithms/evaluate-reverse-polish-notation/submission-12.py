class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for tok in tokens:
            if tok not in "-+*/":
                stack.append(tok)
            else:
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
        return int(stack[-1]) 
            



        