class Solution:
    def romanToInt(self, s: str) -> int:
        literals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        for i in range(len(s)-1,-1,-1):
            cur = literals[s[i]]
            if i < len(s)-1 and cur < literals[s[i+1]]:
                num -= cur
            else:
                num += cur
        return num