class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        inverse = {}
        for i in range(len(nums)):
            if target-nums[i] in inverse:
                return [i,inverse.get(target-nums[i])]
            inverse[nums[i]] = i
        return None