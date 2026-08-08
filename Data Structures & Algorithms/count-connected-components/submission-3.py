class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(list)
        for fro, to in edges:
            nodes[fro].append(to)
            nodes[to].append(fro)
        #swallow a whole piece one at a time
        visited = set()
        
        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for nei in nodes[cur]:
                dfs(nei)

            
        
        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count




        



        