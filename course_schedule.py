class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        preMap={i:[] for i in range(numCourses)}
        for cr,pr in prerequisites:
            preMap[cr].append(pr)
        
        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur]==[]:
                return True
            visited.add(cur)
            for i in preMap[cur]:
                if not dfs(i): return False
            visited.remove(cur)
            preMap[cur]=[]
            return True
        
        for cur in range(numCourses):
            if not dfs(cur): return False
        return True
