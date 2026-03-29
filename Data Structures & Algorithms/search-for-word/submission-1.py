class Solution:
    """
        1. Go through grid if first matching letter is found then start dfs on that track
        2. keep a set of visited i,j so that you don't use same letter again
        3. Keep going dfs on right/left/top/bottom until all matching letters are found
        4. If not found along the track then pop last letter and search in all direction
    """
    def exist(self, board: List[List[str]], word: str) -> bool:

        track = set()
        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, k):
            if k == len(word):
                return True

            if (i < 0 or j < 0 or i == rows or j == cols
             or (i,j) in track or word[k] != board[i][j]):
                return False

            track.add((i,j))
            res = (backtrack(i+1, j, k+1) or 
                    backtrack(i, j+1, k+1) or
                    backtrack(i-1, j, k+1) or
                    backtrack(i, j-1, k+1))
            track.remove((i,j))
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = backtrack(i, j, 0)
                    if res :
                        return res
        return False
        