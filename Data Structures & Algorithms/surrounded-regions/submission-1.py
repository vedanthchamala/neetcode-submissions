class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        safe = set()
        #start at every 0 on the perimeter. mark safe, check 
        #all directions horiontal and vertically, keep making safe until nothing left and then
        #once all the safe indecs are marked, go thorugh and mark everything not safe with 'X'

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X" or (r, c) in safe):
                return 
            safe.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in safe:
                    board[r][c] = "X"
        





        