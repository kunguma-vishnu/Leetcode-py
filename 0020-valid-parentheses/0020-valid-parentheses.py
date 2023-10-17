class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for lt in s:
            if lt in "({[":
                stack.append(lt)
            elif stack:
                last = stack.pop()
                if(last == '(' and lt == ')') or (last == '{' and lt == '}') or (last == '[' and lt == ']'):
                    continue
                else:
                    return False
            else:
                return False
        return len(stack) == 0
