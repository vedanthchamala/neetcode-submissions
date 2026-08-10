class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for fro, to in edges:
            adj[fro].append(to)
            adj[to].append(fro)
        visited = set() #have we been here before

        ## 0, 1, 2, 3, 4 --> if i not in visited: dfs(0) --- visited.add(0, 1, 2)


        ## {[0] = [1], [1] = [2], [0], [2] = [1] }

        def dfs(cur):
            if cur in visited:
                return 
            visited.add(cur)
            for nei in adj[cur]:
                dfs(nei)
        pieces = 0
        #visited = (0, 1, 2)

        #0 0, 1, 2, 3, 4

        for i in range(n): #0->4
            if i not in visited:
                dfs(i)
                pieces = pieces + 1

        return pieces


        
            


        