class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(idx , current , total):
            if total == target:
                result.append(current.copy())
                return
            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                current.append(candidates[i])
                dfs( i + 1 , current , total + candidates[i])
                current.pop()
        dfs(0 , [], 0)
        return result