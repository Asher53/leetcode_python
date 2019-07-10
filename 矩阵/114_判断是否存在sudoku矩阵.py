'''
valid-sudoku
'''

'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character'.'.
'''

'''
判断一个9*9的二维数组是不是一个有效的数独。只用判断有效即可，即题目中的三个条件，不用求解。
'''
'''
把要判断的这些位置的数字取出来，然后用set后的长度是否等于原长度就能知道是不是有重复数字了。题目中已经说了给出的数字只有1~9，所以省掉了很多事。
判断之前需要把’.‘给去掉，因为数字只允许出现一次，而’.'可能出现多次。
时间复杂度是O(N^2)，空间复杂度是O(N).
'''


class Solution(object):
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidNineCell(board)

    def isValidRow(self, board):
        n = len(board)
        for r in range(n):
            # row = [x for x in board[r] if x != '.']
            row = list(filter(lambda x: x != '.', board[r]))
            # 就看有没有重复数字
            if len(set(row)) != len(row):
                return False
        return True

    def isValidCol(self, board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True

    '''
    注意九宫格的写法
    '''

    def isValidNineCell(self, board):
        n = len(board)
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    so = Solution()
    print(so.isValidSudoku(board))
