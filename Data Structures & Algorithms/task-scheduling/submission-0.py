class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)




        cooldown = deque()

        time = 0 

        while max_heap or cooldown:
            time+=1

            while cooldown and cooldown[0][0]<=time:
                ready_time,remaining_count = cooldown.popleft()
                heapq.heappush(max_heap,remaining_count)


            if max_heap:
                count = heapq.heappop(max_heap)

                count+=1

                if count<0:
                    ready_time = time+n+1
                    cooldown.append((ready_time,count))
        return time