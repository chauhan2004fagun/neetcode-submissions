class Solution:
    def isValid(self, s: str) -> bool:
        COP = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in COP:
                if not stack or stack[-1] != COP[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0