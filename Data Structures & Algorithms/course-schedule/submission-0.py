class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()

        def dfs(cur):
            if cur in visiting:
                return False
            if preMap[cur] == []:
                return True

            visiting.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visiting.remove(cur)
            preMap[cur] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True