class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            val = matrix[m // cols][m % cols]

            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False
