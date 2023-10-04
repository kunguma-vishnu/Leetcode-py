class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        past = {0:1}
        for i in range(len(nums)):
            prefixSum = prefixSum + nums[i]
            if prefixSum-k in past:
                count += past.get(prefixSum-k)
            past[prefixSum] = past.get(prefixSum,0)+1
        return count
