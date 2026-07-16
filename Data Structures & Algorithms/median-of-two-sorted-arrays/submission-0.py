class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        m = len(nums1)
        n = len(nums2)

        total = m + n

        half = (total+1)//2

        left = 0
        right = m


        while left<=right:
            i = left+(right-left)//2

            j=half - i

            # nums1 左右边界
            max_left_1 = float("-inf") if i == 0 else nums1[i - 1]
            min_right_1 = float("inf") if i == m else nums1[i]

            # nums2 左右边界
            max_left_2 = float("-inf") if j == 0 else nums2[j - 1]
            min_right_2 = float("inf") if j == n else nums2[j]


            if (max_left_1<=min_right_2 and max_left_2<=min_right_1):
                if total%2==1:
                    return float(max(max_left_1,max_left_2))
                
                left_max = max(max_left_1,max_left_2)
                right_min = min(min_right_1,min_right_2)
                return (left_max+right_min)/2.0
            elif max_left_1>min_right_2:
                right = i -1
            else:
                left=i+1
        raise ValueError("At least one input array must be non-empty.")
        
