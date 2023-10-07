class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumArr = sum(nums[:k])
        maxArr = sumArr
        for i in range(k,len(nums)):
            sumArr += nums[i] - nums[i-k]
            maxArr = max(maxArr,sumArr)
        return maxArr/k