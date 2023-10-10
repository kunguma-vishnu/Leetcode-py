class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        threeLowToHigh=nums[-1] * nums[-2] * nums[-3]
        threeHighToLow=nums[0] * nums[1] * nums[-1]
        maxOfThree=max(threeLowToHigh, threeHighToLow)
        
        return maxOfThree
            
