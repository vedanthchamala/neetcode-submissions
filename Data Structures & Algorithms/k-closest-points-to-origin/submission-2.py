import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        res = []
        for x, y in points:
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(dist, [distance, (x, y)])
        while len(res) != k:
            res.append(heapq.heappop(dist)[1])
        return res
        



        