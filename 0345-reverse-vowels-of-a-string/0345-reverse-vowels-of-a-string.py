class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for letter in s:
            if letter in vowels:
                stack.append(letter)
        res = []
        for letter in s:
            if letter in vowels:
                res.append(stack.pop())
            else:
                res.append(letter)
        return ''.join(res)