class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif stack:
                cur = stack.pop()
                if (cur == "(" and ch == ")") or (cur == "[" and ch == "]") or (cur == "{" and ch == "}"):
                    continue
                else:
                    return False
            else:
                return False
        return len(stack) == 0