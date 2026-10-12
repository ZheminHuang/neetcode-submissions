class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i,current_xor):
            if i == len(nums):
                return current_xor
            
            skip = dfs(i+1,current_xor)

            take = dfs(i+1,current_xor^nums[i])

            return skip+take
        
        return dfs(0,0)