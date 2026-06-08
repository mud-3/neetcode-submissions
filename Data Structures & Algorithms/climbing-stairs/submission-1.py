class Solution:
    def climbStairs(self, n: int) -> int:
        # 矩陣相乘函數
        def multiply(A, B):
            C = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        C[i][j] += A[i][k] * B[k][j]
            return C

        # 矩陣快速冪
        def matrix_pow(A, p):
            res = [[1, 0], [0, 1]] # 單位矩陣 (Identity Matrix)
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res

        if n == 0: return 0
        if n == 1: return 1
        
        # Fibonacci 嘅變換矩陣
        T = [[1, 1], [1, 0]]
        
        # 我哋要計 T 嘅 n 次方
        # 留意：climbStairs(n) 其實係 Fibonacci 第 n+1 項
        result_matrix = matrix_pow(T, n)
        
        # 根據公式，F(n+1) 會喺結果矩陣嘅 [0][0] 位置
        return result_matrix[0][0]