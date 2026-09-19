class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board) # rows = 0 1 2
        cols = len(board[0]) # cols = 0 1 2 3

        visited = set() # { }

        def dfs(r,c,index): # index = which char of word we need
            if index == len(word): # 3 = 3 # word = "CAT"
                return True
            # make sure the r and c remain with in the board matrix
            if r < 0 or r>=rows or c <0 or c>= cols: # false or false or false or true
                return False
            if (r,c) in visited:
                return False
            # check if board[x][y] contain the word[0] 
            if board[r][c] != word[index]:
                return False
            visited.add((r,c))

            Found = (
                dfs(r + 1 , c , index + 1) or
                dfs(r - 1 , c , index + 1) or
                dfs(r , c + 1 , index + 1) or
                dfs(r , c - 1 , index + 1) 
            )
            visited.remove((r,c))
            return Found

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False