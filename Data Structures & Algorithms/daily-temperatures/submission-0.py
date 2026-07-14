class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for current_day,current_tmp in enumerate(temperatures):
            while (stack and current_tmp > temperatures[stack[-1]]):
                previous_day = stack.pop()
                result[previous_day]= current_day - previous_day
            
            stack.append(current_day)
        return result