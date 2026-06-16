class Solution:
    #Bitmasking method
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #create initial list to record upcoming condition, note that we are using binary
        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue

                #create a binary mask by shifting 1 by cell value places, e.q. if value = 5, mask = 00100000
                mask = 1 << int(cell) - 1
                square = i // 3 * 3 + j // 3

                #use and operation to check is that digit already been recorded (duplicate)
                if (rows[i] & mask) or (columns[j] & mask) or (squares[square] & mask):
                    return False

                #use or operation to record that bit as 1 (visited)
                rows[i] |= mask
                columns[j] |= mask
                squares[square]|= mask
        
        return True