class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=True
        if len(s)!=len(t):
            return False
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
            if s.count(i)!=t.count(i):
                return False
        return True