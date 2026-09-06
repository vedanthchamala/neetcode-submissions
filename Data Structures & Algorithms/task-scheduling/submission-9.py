class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for tsk in tasks:
            freq[tsk] = freq.get(tsk, 0) + 1
        freqs = [count for item, count in freq.items()]
        wait = collections.deque()
        heapq.heapify_max(freqs)
        cycles = 0
        while wait or freqs:
            cycles += 1
            if freqs:
                cur_task = heapq.heappop_max(freqs)
                cur_task -= 1
                if cur_task > 0:
                    wait.append([cur_task, n + cycles])

            if wait and wait[0][1] == cycles:
                back = wait.popleft()[0]
                heapq.heappush_max(freqs, back)

        return cycles

                











                










        