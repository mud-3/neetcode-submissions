class Solution:
    #optimised O(n) solution
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                index = stack.pop()[0]
                output[index] = (i - index)

            stack.append((i, temperature))

        return output