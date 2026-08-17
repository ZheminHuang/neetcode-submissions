class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        island = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]=="1":
                    island +=1
                    queue = deque()

                    queue.append((r,c))

                    grid[r][c]="0"

                    while queue:
                        row,col = queue.popleft()

                        for dc,dr in directions:
                            nr = row+dr
                            nc = col+dc
                            if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1"):
                                grid[nr][nc]="0"
                                queue.append((nr,nc))
        return island


