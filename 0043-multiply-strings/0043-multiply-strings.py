class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res, pos = 0, len(num1 + num2) - 2
        for i1, n1 in enumerate(map(int, num1)):
            for i2, n2 in enumerate(map(int, num2)):
                res += n1 * n2 * 10 ** (pos - (i1 + i2))
        return str(res)