class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #need to first get our entire adjacency list so we can go through dfs
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        parent = {}

        def dfs(node, par):
            visited.add(node)
            parent[node] = par
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visited:
                    return (node, nei)
                found = dfs(nei, node)
                if found:
                    return found
            return None
        
        start, end = dfs(1, -1)

        cycle = {end}
        cur = start
        while cur != end:
            cycle.add(cur)
            cur = parent[cur]
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        
                

        