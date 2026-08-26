class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp= {}

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            

            longest =1

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if (0<=nr <rows and 0<=nc <cols and matrix[nr][nc] > matrix[r][c]):
                    longest = max(longest, 1+dfs(nr,nc))
            

            dp[(r,c)] = longest

            return longest

        result = 0

        for r in range(rows):
            for c in range(cols):
                result = max(result,dfs(r, c))

        return result