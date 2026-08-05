class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=[]

        for x,y in points:
            distance = x*x+y*y
            heapq.heappush(min_heap,(distance,x,y))

        result = []
        
        for _ in range(k):
            distance,x,y = heapq.heappop(min_heap)
            result.append([x,y])
        return result