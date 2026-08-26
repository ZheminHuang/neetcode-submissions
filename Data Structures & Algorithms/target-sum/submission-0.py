class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={0:1}

        for num in nums:
            next_dp = {}

            for total,ways in dp.items():
                plus = total +num
                minus = total -num

                next_dp[plus] = next_dp.get(plus,0)+ways
                next_dp[minus] = next_dp.get(minus,0)+ways
            
            dp= next_dp
        
        return dp.get(target,0)