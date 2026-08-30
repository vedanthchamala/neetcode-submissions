class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        dist = 0
        def addCell(r, c):
            if (r >= rows or c >= cols or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == -1):
                return
            queue.append([r, c])
            visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


        
        
        
                    
        