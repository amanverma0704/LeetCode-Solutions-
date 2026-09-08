class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            ans = 0
            while num != 0:
                rem = num % 10
                num //= 10  # Use integer division in Python
                ans += rem
            num = ans
        return num
