class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        exor = 0
        for n in nums:
            exor ^= n
        return exor