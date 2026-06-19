class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if stack and bracket in closeToOpen:
                if stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return not stack