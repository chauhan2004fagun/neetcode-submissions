class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result =[]
        board = [ ["."] * n for _ in range(n)]
        def issafe(row,col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
                
            r = row - 1
            c = col - 1
            while r>= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r-=1
                c-=1
            r = row - 1
            c = col + 1
            while r>= 0 and c<n:
                if board[r][c] == "Q":
                    return False
                r-=1
                c+=1
            return True

        def backtrack(row):
            if row == n:
                arrangement = []
                for r in range(n):
                    arrangement.append("".join(board[r]))
                result.append(arrangement)
                return
            for col in range(n):
                if not issafe(row,col):
                    continue
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."
        backtrack(0)
        return result