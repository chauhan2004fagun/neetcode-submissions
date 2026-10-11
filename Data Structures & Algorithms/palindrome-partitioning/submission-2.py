# aab  palindrome a - a,  b - b, a - a or aa  b 
#
#
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def palindrome(word):
            return word == word[::-1]
        def dfs(start , current):
            if start == len(s):
                result.append(current.copy())
                return 
            for end in range(start , len(s)):
                part = s[start:end+1] # s[0 , 0 + 1] for end = 0
                if not palindrome(part):
                    continue
                current.append(part)
                dfs(end +1 , current)
                current.pop()
        dfs(0,[])
        return result
                
            