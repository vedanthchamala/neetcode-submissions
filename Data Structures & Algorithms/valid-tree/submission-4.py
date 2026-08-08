class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = defaultdict(list)
        for fro, to in edges:
            nodes[fro].append(to)
            nodes[to].append(fro)
        path = set()

        def dfs(cur, prev):
            if cur in path:
                return False

            path.add(cur)
            
            for nei in nodes[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        return dfs(0, -1) and len(path) == n
            
        