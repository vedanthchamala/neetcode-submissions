class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-1 * num for num in nums]
        heapq.heapify(neg)
        for _ in range(k - 1):
            heapq.heappop(neg)
        return -1 * neg[0]
        