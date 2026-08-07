class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def addCell(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit):
                return
            queue.append([r, c])
            visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))
                    

        dist = 0
        
        while queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
                



        