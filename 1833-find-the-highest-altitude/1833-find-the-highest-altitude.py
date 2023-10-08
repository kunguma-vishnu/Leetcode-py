class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = [0]
        prev = 0
        maxGain = 0
        for num in gain:
            prev = prev + num
            maxGain = max(maxGain,prev)
        return maxGain