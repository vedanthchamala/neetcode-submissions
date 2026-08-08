class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = defaultdict(list)
        for course, pre in prerequisites:
            pres[course].append(pre)
        finished = set()
        path = set()

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
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        