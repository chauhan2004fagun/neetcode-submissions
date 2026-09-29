# heap = [-4,b ,(-3,a), (-2,a)] 
# 
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a> 0:
            heapq.heappush(heap , (-a, 'a'))
        if b>0:
            heapq.heappush(heap , (-b , 'b'))
        if c > 0:
            heapq.heappush(heap , (-c, 'c'))
        ans = []
        while heap:
            cnt , ch = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                if not heap:
                    break
                cnt2 , ch2 = heapq.heappop(heap)

                ans.append(ch2)
                cnt2+=1

                if cnt2<0:
                    heapq.heappush(heap , (cnt2 , ch2))
                heapq.heappush(heap , (cnt , ch))
            else:
                ans.append(ch)
                cnt+=1

                if cnt<0:
                    heapq.heappush(heap , (cnt , ch))
        return ''.join(ans)
