class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append((temperatures[0], 0))
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            if stack and temp <= stack[-1][0]:
                stack.append((temp, i))
            elif stack and temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    index = stack.pop()[1]
                    res[index] = i - index
                stack.append((temp, i))
        return res




        # okay, so if i see a temp that is less than my most prev, push it onto the stack, but if i see an element that 
            







        