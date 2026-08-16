class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((query,index) for index,query in enumerate(queries))

        result = [-1]*len(queries) 
        heap=[]

        i = 0 

        for query,index in sorted_queries:

            while (i<len(intervals) and intervals[i][0]<=query):
                left,right=intervals[i]

                length =right-left+1

                heapq.heappush(heap,(length,right))

                i+=1

            while heap and heap[0][1]<query:
                heapq.heappop(heap)
            if heap:
                result[index]=heap[0][0]
        return result