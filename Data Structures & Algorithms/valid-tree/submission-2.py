class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for node, to in edges:
            adj[node].append(to)
            adj[to].append(node)
        path = set()

        

        def dfs(cur, prev):
            if cur in path:
                return False

            
            path.add(cur)

            for nei in adj[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        return dfs(0, -1) and len(path) == n
        
            

                

            







        