class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = []
        pos = sorted(zip(position, speed), reverse = True)

        for p, s in pos:
            time_needed = (target - p) / s
            if stack and stack[-1] >= time_needed:
                continue
            stack.append(time_needed)
        return len(stack)





        