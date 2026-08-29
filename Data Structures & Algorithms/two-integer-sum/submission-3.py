class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i , num in enumerate(nums):
            cop = target - num

            if cop in hash_map:
                return[hash_map[cop],i]
            hash_map[num] = i
        return []