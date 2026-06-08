class Solution:
    def isValid(self, s: str) -> bool:
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