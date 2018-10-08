class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        # stores every correct board configurations
        solutions = []
        
        # recursive backtracking solution
        def backtrack(board):
            # maximum recursion depth, we have a solution !
            if len(board) == n:
                pretty_board = []
                for row in board:
                    pretty_row = "." * row + "Q" + "." * (n - row - 1)
                    pretty_board.append(pretty_row)
                solutions.append(pretty_board)
            else:
                # consider placing a queen on each column of the current row
                for pos in range(n):
                    ok = True
                    # check previous rows : skip columns where there is already a queen, and check diagonals
                    for i in range(len(board)):
                        if (pos == board[i]) or (abs(board[i] - pos) == abs(i - len(board))):
                            ok = False
                            break
                    # place the queen on this column and carry on to the next row
                    if ok:
                        backtrack(board + [pos])
                        
        backtrack([])
        return solutions