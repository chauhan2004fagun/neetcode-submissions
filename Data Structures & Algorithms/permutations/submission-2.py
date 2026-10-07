class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        u = [False] * len(nums)
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return 
            for i in range(len(nums)):
                if u[i]:
                    continue
                u[i] = True
                current.append(nums[i])
                backtrack(current)

                current.pop()
                u[i] = False
        backtrack([])
        return result