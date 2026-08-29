class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}

        for num in nums:
            hash_map[num]= hash_map.get(num,0)+1

        heap=[]
        for num , freq in hash_map.items():
            heapq.heappush(heap,(freq, num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]