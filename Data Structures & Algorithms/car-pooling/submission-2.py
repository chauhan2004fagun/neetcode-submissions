class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        heap = []
        cp = 0

        for p , froml , tol in trips:
            while heap and heap[0][0] <= froml:
                dropof , nump = heapq.heappop(heap)
                cp -= nump
            
            cp += p

            if cp > capacity:
                return False

            heapq.heappush(heap , (tol , p)) 
        return True