class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        res = 0
        odd = False

        for ch in count:
            if count[ch] % 2 == 0:
                res += count[ch]
            else:
                res += count[ch] - 1
                odd = True

        if odd:
            res += 1

        return res