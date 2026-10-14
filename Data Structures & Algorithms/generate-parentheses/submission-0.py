class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(op , cl , current):
            if len(current) == 2*n:
                result.append("".join(current))
                return 
            if op < n:
                current.append("(")
                backtrack(op + 1 , cl , current)
                current.pop()
            if cl < op:
                current.append(")")
                backtrack(op , cl + 1 , current)
                current.pop()
        backtrack(0 , 0 , [])
        return result