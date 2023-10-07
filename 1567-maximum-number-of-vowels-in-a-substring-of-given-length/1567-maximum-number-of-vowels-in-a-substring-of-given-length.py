class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCount = curCount = 0
        vowels = ['a','e','i','o','u']
        for i in range(len(s)):
            if s[i] in vowels:
                curCount += 1
            if i>=k:
                if s[i-k] in vowels:
                    curCount -= 1
            maxCount = max(curCount,maxCount)
        return maxCount