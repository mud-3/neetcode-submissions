class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #optimised solution
        nums = []
        
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                subtrahend, minuend = nums.pop(), nums.pop()
                nums.append(minuend - subtrahend)
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            elif token == "/":
                divisor, dividend = nums.pop(), nums.pop()
                nums.append(int(dividend / divisor))
            else:
                nums.append(int(token))
        return nums[0]