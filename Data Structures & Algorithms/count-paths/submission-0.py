class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        rows, cols = m, n
        paths = 0

        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return 1
            if r >= rows or c >= cols:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            memo[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[r][c]
        return dfs(0, 0)




        