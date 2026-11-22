class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
        task_counts = list(freqs.values())
        heapq.heapify_max(task_counts)
        queue = collections.deque()
        cycles = 0
        while task_counts or queue:
            if task_counts:
                nxt = heapq.heappop_max(task_counts)
                nxt -= 1
                if nxt > 0:
                    queue.append((nxt, cycles + n))
            if queue and queue[0][1] == cycles:
                ready = queue.popleft()
                heapq.heappush_max(task_counts, ready[0])
            cycles += 1
        return cycles


        