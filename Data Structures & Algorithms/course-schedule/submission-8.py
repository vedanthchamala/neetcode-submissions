class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = defaultdict(list)
        for course, pre in prerequisites:
            pres[course].append(pre)
        path = set()
        finished = set()
        
        def canFinish(cur):
            if cur in finished:
                return True
            if cur in path:
                return False
            path.add(cur)
            for pre in pres[cur]:
                if not canFinish(pre):
                    return False
            path.remove(cur)
            finished.add(cur)
            return True
        for i in range(numCourses):
            if not canFinish(i):
                return False
        return True

        
        