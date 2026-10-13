class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res




        # okay, so if i see a temp that is less than my most prev, push it onto the stack, but if i see an element that 
            







        