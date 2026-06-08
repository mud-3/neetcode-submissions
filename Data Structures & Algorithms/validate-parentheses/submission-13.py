class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []

        if len(s) % 2:
            return False

        for p in s:
            if p not in close_to_open:
                stack.append(p)
            elif stack and close_to_open[p] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack
        