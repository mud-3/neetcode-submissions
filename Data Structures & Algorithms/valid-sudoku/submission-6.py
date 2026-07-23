class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    square = i // 3 * 3 + j // 3
                    if cell in rows[i] or cell in columns[j] or cell in squares[square]:
                        return False
                    rows[i].add(cell)
                    columns[j].add(cell)
                    squares[square].add(cell)
        
        return True
