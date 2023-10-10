class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float(-inf)
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(maxSum,curSum)
            if curSum < 0:
                curSum = 0
        return maxSum