class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        a = 0
        b = 1
        c = 2
        for i in range(len(s)-2):
            if s[a] != s[b] and s[b] != s[c] and s[a] != s[c]:
                count += 1
            a += 1
            b += 1
            c += 1
        return count