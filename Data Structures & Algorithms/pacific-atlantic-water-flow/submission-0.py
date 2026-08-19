class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])


        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def bfs(queue,visited):
            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if (0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        for r in range(rows):
            pacific_queue.append((r,0))
            pacific.add((r,0))

            atlantic_queue.append((r, cols - 1))
            atlantic.add((r, cols - 1))

        for c in range(cols):
            pacific_queue.append((0, c))
            pacific.add((0, c))

            atlantic_queue.append((rows - 1, c))
            atlantic.add((rows - 1, c))

        
        bfs(pacific_queue,pacific)
        bfs(atlantic_queue, atlantic)

        result = []


        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result