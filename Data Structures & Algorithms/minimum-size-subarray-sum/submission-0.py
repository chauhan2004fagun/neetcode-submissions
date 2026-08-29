class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum=0
        l=0
        minimum=float('inf')
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum >= target:
                curr_len=r-l+1
                minimum = min(minimum, curr_len)
                curr_sum -=nums[l]
                l+=1
        if minimum == float('inf'):
            return 0
        return minimum