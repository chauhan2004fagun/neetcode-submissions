# p , floc , tloc -> [4 , 1, 2]
# heap = [2,4]
# cp = 4
#
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        heap = []
        cp = 0
        for p , floc , tloc in trips:
            while heap and heap[0][0] <= floc:  
                droploc , nump = heapq.heappop(heap)
                cp = cp - nump
    
            cp += p
            
            if cp > capacity:
                return False
            heapq.heappush(heap , (tloc , p))
        return True