class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # TC =. O(mn * 3^ l) where l is length of word
        # Sc = O(l)
        if board is None or len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def backtrack(board, word,ind,r,c):
           
            #base
            if ind ==len(word):
                return True
            if (r < 0 or c <0 or r == m or c ==n or
               board[r][c] != word[ind]):
                return False
            
            #logic
            #action
            # mark the starting point
            ch = board[r][c]
            board[r][c] = '#'
            for d in dirs:
                row = r + d[0]
                col = c + d[1]
                
                #recurse
                if backtrack(board, word,ind + 1,row,col):
                    return True
            
            #backtrack
            board[r][c] = ch
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(board,word, 0, i,j):
                        return True
        
        return False
        
