class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        combination = []


        def dfs(start:int, remaining :int)->None:
            if remaining ==0:
                result.append(combination.copy())
                return 
            
            for i in range(start,len(candidates)):

                if i>start and candidates[i]==candidates[i-1]:
                    continue
                
                if candidates[i]>remaining:
                    break
                
                combination.append(candidates[i])

                dfs(i+1,remaining-candidates[i])

                combination.pop()
        dfs(0,target)
        return result