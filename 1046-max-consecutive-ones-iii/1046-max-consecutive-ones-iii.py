class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        maxCount = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count>k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            maxCount = max(maxCount,r-l+1)
        return maxCount