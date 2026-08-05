class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        freq_list = [freq for freq in freq.values()]
        heapq.heapify_max(freq_list)
        jail = collections.deque()
        cycles = 0

        while freq_list or jail:
            cycles += 1
            if freq_list:
                cur = heapq.heappop_max(freq_list)
                cur -= 1

                if cur > 0:
                    jail.append([cur, cycles + n])
            if jail and jail[0][1] == cycles:
                ready = jail.popleft()[0]
                heapq.heappush_max(freq_list, ready)

        return cycles
                
            
                

                
            
            
        
        

        