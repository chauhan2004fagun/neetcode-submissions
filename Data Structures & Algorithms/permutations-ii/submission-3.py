# index = 0 1 2
# nums =  1 1 2
# used =  f f f
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False] * len(nums)
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue 
                used[i] = True
                current.append(nums[i])
                backtrack(current)

                current.pop()
                used[i] = False
        backtrack([])
        return result             