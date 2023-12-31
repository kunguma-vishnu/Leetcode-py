class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies >= maxCandy:
                res += [True]
            else:
                res += [False]
        return res