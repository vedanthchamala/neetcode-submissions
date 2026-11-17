class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        n = len(gas)
        total = 0
        tank = 0
        for i in range(n):
            tank += gas[i]
            tank -= cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1



                


        