class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
            print(nums)
        
        return nums[0]