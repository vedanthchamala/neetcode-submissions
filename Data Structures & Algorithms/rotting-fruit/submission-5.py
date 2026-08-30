class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        mins = 0


        def rotFruit(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r, c) in visited):
                return 
            queue.append([r, c])
            visited.add((r, c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r, c))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                rotFruit(r + 1, c)
                rotFruit(r - 1, c)
                rotFruit(r, c + 1)
                rotFruit(r, c - 1)
            if queue:
                mins += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return mins


                