class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def ispalindrome(word):
            return word == word[::-1]
        def backtrack(start , current):
            if start == len(s):
                result.append(current.copy())
                return 
            for end in range(start , len(s)):
                part = s[start:end+1]

                if not ispalindrome(part):
                    continue
                current.append(part)
                backtrack(end + 1 , current)
                current.pop()
        backtrack(0 , [])
        return result