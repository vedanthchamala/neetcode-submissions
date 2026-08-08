class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = defaultdict(list)
        for course, pre in prerequisites:
            pres[course].append(pre)
        order = []
        finished = set()
        path = set()

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
            order.append(cur)
            return True



        for course in range(numCourses):
            if canFinish(course) == False:
                return []
        return order





        