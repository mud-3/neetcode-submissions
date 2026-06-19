class Solution:
    def isValid(self, s: str) -> bool:
        opened = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if stack and bracket in opened:
                if stack[-1] == opened[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return not stack