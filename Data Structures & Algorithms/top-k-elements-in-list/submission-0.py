class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        bucket = [[] for _ in range(len(nums)+1)]

        for n, freq in count.items():
            bucket[freq].append(n)
        
        result = []

        for freq in range(len(bucket)-1,0,-1):
            for n in bucket[freq]:
                result.append(n)

                if len(result) == k:
                    return result
        return result