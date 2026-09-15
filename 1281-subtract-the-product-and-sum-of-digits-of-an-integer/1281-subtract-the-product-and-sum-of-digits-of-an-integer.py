class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = n
        product = 1
        sum = 0
        while num>0:
            ld = num%10
            num //= 10
            product *= ld
            sum += ld
        return product - sum

