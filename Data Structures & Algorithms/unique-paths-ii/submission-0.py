class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])




        if obstacleGrid[0][0]==1:
            return 0
        
        dp = [[0]*cols for _ in range(rows)]

        dp[0][0]=1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c]==1:
                    dp[r][c]=0
                    continue
                if r>0:
                    dp[r][c]+=dp[r-1][c]
                if c>0:
                    dp[r][c]+=dp[r][c-1]
        

        return dp[rows-1][cols-1]