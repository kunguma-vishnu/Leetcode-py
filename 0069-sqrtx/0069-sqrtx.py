class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start = 0
        end = x
        while abs(start-end) != 1:
            mid = (start+end)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                end = mid
            else:
                start = mid
        return start