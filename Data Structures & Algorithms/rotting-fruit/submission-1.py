class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()

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
        
        mins = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = 2
                elimFruit(row + 1, col)
                elimFruit(row - 1, col)
                elimFruit(row, col + 1)
                elimFruit(row, col - 1)
            if queue:
                mins += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return mins



        