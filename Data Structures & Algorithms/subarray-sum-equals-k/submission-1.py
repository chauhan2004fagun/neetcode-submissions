class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cursum=0
        prefixsum={0:1}
        for num in nums:
            cursum+=num
            diff=cursum-k
            res+=prefixsum.get(diff,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return res