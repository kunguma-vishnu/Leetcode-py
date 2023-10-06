class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        cur = 1
        for i in range(len(nums)):
            product[i] = cur
            cur *= nums[i]
        cur = 1
        for i in range(len(nums)-1,-1,-1):
            product[i] *= cur
            cur *= nums[i]
        return product