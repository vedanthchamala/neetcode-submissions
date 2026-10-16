class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        new = zip(position, speed)
        new = sorted(new, reverse = True)
        stack = []

        for pos, speed in new:
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)


        