class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        permutation = []

        used = set()

        def dfs():
            if len(permutation)==len(nums):
                result.append(permutation.copy())
                return 
            
            for num in nums:
                if num in used:
                    continue
                
                permutation.append(num)
                used.add(num)

                dfs()

                permutation.pop()
                used.remove(num)

        dfs()
        return result
