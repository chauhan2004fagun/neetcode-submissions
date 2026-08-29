class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i , n in enumerate(nums):
            if n in nums[i+1:i+k+1]:
                return True
        return False