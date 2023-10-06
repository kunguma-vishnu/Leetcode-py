class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3: return n-1
        quotient = n//3
        product = 3**quotient
        if n%3 == 1:
            product //= 3
            product *= 4
        elif n%3 == 2:
            product *= 2
        return product
