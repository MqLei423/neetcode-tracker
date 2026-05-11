class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visited,visiting = set(),set()

        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res