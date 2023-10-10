class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter != ']':
                stack.append(letter)
            else:
                res = ""
                while stack[-1] != '[':
                    res += stack.pop()
                stack.pop()
                n = ""
                while stack and stack[-1].isdigit():
                    n+=stack.pop()
                stack.append(res*int(n[::-1]))
        return ''.join([word[::-1] for word in stack])