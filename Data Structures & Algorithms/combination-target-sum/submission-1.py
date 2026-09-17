class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]] :
        result = []
        nums.sort()
        def backtrack(i , current , total):
            if total == target:
                result.append(current.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                current.append(nums[j])
                backtrack(j , current , total + nums[j])
                current.pop()
        backtrack(0 , [] , 0)
        return result