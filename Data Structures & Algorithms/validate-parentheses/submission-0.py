class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        COP = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in COP:
                if stack and stack[-1] == COP[c]:
                     stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack==[]:
            return True
        else:
            return False