class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #optimised solution
        nums = []
        
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                nums.append(-nums.pop() + nums.pop()) #first number come out is the one that deduct the value
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            elif token == "/":
                nums.append(int((1 / nums.pop()) * nums.pop())) #first number come out is the denominator
            else:
                nums.append(int(token))
        return nums[0]