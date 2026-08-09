class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visit.add((r, c))

        def elimFruit(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] != 1):
                return
            queue.append([r, c])
            visit.add((r, c))
        minutes = 0
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                elimFruit(r + 1, c)
                elimFruit(r - 1, c)
                elimFruit(r, c + 1)
                elimFruit(r, c - 1)
            if queue:
                minutes += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes
    
            

        

            
        