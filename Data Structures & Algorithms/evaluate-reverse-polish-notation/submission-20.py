class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #unoptimised solution, add, sub, mul, div 四個輔助函數，雖然可讀性好，但每次調用都會產生函數棧幀（Stack frame）的額外開銷
        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b

        def mul(a, b):
            return a * b

        def div(a, b):
            return int(a / b)

        signs = {"+": add, "-": sub, "*": mul, "/": div}
        nums = []
        
        for token in tokens:
            if token in signs:
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(signs[token](num1, num2))
            else:
                nums.append(int(token))
        
        return nums[0]