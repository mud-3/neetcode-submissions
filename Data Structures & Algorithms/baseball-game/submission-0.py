class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []

        for op in operations:
            match op:
                case "+":
                    points.append(points[-1] + points[-2])
                case "C":
                    points.pop()
                case "D":
                    points.append(points[-1] * 2)
                case _:
                    points.append(int(op))
        
        return sum(points)