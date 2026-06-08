class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False

        closeBrackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char not in closeBrackets:
                stack.append(char)
            elif stack and closeBrackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack