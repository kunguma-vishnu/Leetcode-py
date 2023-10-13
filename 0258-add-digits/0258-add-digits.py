class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s)>1:
            sumOfNum = 0
            for n in s:
                sumOfNum += int(n)
            s = str(sumOfNum)
        return int(s)