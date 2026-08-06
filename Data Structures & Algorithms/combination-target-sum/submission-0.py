class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(index:int,remaining:int)->None:
            if remaining ==0:
                result.append(combination.copy())
                return 
            
            if index == len(nums) or remaining<0:
                return 
            
            combination.append(nums[index])
            dfs(index,remaining-nums[index])

            combination.pop()

            dfs(index+1,remaining)
        dfs(0,target)
        return result
