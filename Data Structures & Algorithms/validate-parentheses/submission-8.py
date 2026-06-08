class Solution:
    def isValid(self, s: str) -> bool:
        closeBrackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in closeBrackets:
                if stack and closeBrackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack