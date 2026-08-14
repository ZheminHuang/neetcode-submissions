class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i,interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                result.append(interval)
            
            elif newInterval[1]<interval[0]:
                return result+[newInterval]+intervals[i:]
            
            else:
                newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
        return result+[newInterval]