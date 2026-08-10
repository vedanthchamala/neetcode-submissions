class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = defaultdict(list)
        for course, pre in prerequisites:
            pres[course].append(pre)
        finished = set()
        path = set()
        order = []
        def dfs(cur):
            if cur in finished:
                return True
            if cur in path:
                return False
            path.add(cur)
            for pre in pres[cur]:
                if not dfs(pre):
                    return False
            path.remove(cur)
            finished.add(cur)
            order.append(cur)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return order
            
        