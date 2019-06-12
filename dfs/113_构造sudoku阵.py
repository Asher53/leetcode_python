'''
sudoku-solver
'''

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character'.'.
You may assume that there will be only one unique solution.
'''


class Solution:
    def check(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        # 检查一行是否符合条件
        for row in range(9):
            if board[row][y] == tmp:
                return False
        # 检查一列是否符合条件
        for col in range(9):
            if board[x][col] == tmp:
                return False
        # 检查3x3小宫格是否符合条件
        for row in range(3):
            for col in range(3):
                if board[(x // 3) * 3 + row][(y // 3) * 3 + col] == tmp:
                    return False
        board[x][y] = tmp
        return True

    def dfs(self, board):
        # 填满格子后就会停止dfs
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row, col, board) and self.dfs(board):
                            return True
                        board[row][col] = '.'
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
    print(so.dfs(board))

    for v in board:
        print(v)
