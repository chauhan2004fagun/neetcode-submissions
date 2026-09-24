class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        for count in freq.values():
            heapq.heappush(heap , -count)
        q = deque()
        time = 0
        while q or heap:
            time+=1

            if q and q[0][1] == time:
                count , readytime = q.popleft()
                heapq.heappush(heap , count)
            
            if heap :
                count = heapq.heappop(heap)
                count +=1

                if count != 0:
                    q.append((count , time + n +1))
        return time