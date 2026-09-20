class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        digit = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        def backtrack(i , current):
            if len(current) == len(digits):
                result.append("".join(current))
                return 
            for c in digit[digits[i]]:
                current.append(c)
                backtrack(i + 1 , current)
                current.pop()
        backtrack(0 , [])
        return result