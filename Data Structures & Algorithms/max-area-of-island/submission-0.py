class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols =  len(grid[0])


        max_area = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        for r in range(rows):
            for c in range(cols):

                if grid[r][c]== 1:
                    queue=deque([(r,c)])
                    grid[r][c]=0

                    area = 0

                    while queue:
                        row,col = queue.popleft()
                        area+=1

                        for dr,dc in directions:
                            nr = row+dr
                            nc = col+dc

                            if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                                grid[nr][nc]=0
                                queue.append((nr,nc))
                    
                    max_area = max(max_area,area)
        return max_area