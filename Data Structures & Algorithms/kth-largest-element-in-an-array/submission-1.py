# 23154 - [1 2 3 4 5]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap , num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]