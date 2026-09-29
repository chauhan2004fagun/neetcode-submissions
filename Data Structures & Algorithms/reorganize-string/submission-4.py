class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap=[]
        for ch,cnt in freq.items():
            heapq.heappush(heap ,( -cnt, ch))
        ans = []
        while heap:
            cnt ,ch = heapq.heappop(heap)
            if len(ans) >=1 and ans[-1] == ch:
                if not heap:
                    return ("")
                cnt2 , ch2 = heapq.heappop(heap)
                ans.append(ch2)
                cnt2 +=1
                if cnt2 < 0 :
                    heapq.heappush(heap , (cnt2 , ch2))
                heapq.heappush(heap , (cnt , ch))
            else:
                ans.append(ch)
                cnt += 1
                if cnt<0:
                    heapq.heappush(heap , (cnt , ch))
        return ''.join(ans)
