class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ind = 0
        element = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > element:
                ind = i
                element = nums[i]
        return ind