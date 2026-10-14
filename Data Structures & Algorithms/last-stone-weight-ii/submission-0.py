class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2

        dp = [False]*(target+1)

        dp[0] = True

        for weight in stones:
            for s in range(target,weight-1,-1):
                dp[s] = dp[s] or dp[s-weight]
        

        for s in range(target,-1,-1):
            if dp[s]:
                return total-2*s