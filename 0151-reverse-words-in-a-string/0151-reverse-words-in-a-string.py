class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split(" ")
        stack = []
        for token in tokens:
            if token != '':
                stack.append(token)
        print(stack)
        res = []
        while stack != []:
            res.append(stack.pop())
        return " ".join(res)