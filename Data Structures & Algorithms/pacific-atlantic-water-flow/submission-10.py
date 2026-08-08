class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        alt = set()

        def flow(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight or (r, c) in visit):
                return
            visit.add((r, c))
            flow(r + 1, c, visit, heights[r][c])
            flow(r - 1, c, visit, heights[r][c])
            flow(r, c + 1, visit, heights[r][c])
            flow(r, c - 1, visit, heights[r][c])

        
        for r in range(rows):
            flow(r, 0, pac, heights[r][0])
            flow(r, cols - 1, alt, heights[r][cols - 1])
        for c in range(cols):
            flow(0, c, pac, heights[0][c])
            flow(rows - 1, c, alt, heights[rows - 1][c])

        return [[r, c] for (r, c) in alt & pac]
            
        