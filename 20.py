class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        closingDict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for brack in s:
            if brack not in closingDict:
                stack.append(brack)
            else:
                if len(stack) == 0 or closingDict[brack] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
