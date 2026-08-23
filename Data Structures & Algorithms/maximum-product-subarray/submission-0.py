class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]


        for num in nums[1:]:
            new_max = max(num,current_max*num,current_min*num)

            new_min = min(num,current_max*num,current_min*num)

            current_max = new_max
            current_min = new_min

            result = max(result,current_max)
        
        return result
        