class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        done = set()

        
        def safe(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X" or (r, c) in done):
                return 
            done.add((r, c))
            safe(r + 1, c)
            safe(r - 1, c)
            safe(r, c + 1)
            safe(r, c - 1)
        
        for r in range(rows):
            safe(r, 0)
            safe(r, cols - 1)
        for c in range(cols):
            safe(0, c)
            safe(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in done:
                    board[r][c] = "X"





        