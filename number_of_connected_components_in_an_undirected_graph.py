class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit=[False]*n
        res=0

        def dfs(node):
            for i in adj[node]:
                if not visit[i]:
                    visit[i]=True
                    dfs(i)

        for node in range(n):
            if not visit[node]:
                visit[node]=True
                dfs(node)
                res+=1
        return res

            
        