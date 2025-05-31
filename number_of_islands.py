class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        islands=0

        def bfs(r,c):
            q=deque()
            grid[r][c]="0"
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if (r<0 or c<0 or
                    r>=rows or c>=cols or 
                    grid[r][c]=="0"):
                        continue
                    q.append((r,c))
                    grid[r][c]="0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands
        