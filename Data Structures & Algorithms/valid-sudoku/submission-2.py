class Solution:
    #Bitmasking method
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    value = int(cell)
                    mask = 1 << value
                    square = i // 3 * 3 + j // 3
                    if (rows[i] & mask) or (columns[j] & mask) or (squares[square] & mask):
                        return False
                    rows[i] |= mask
                    columns[j] |= mask
                    squares[square]|= mask
        
        return True