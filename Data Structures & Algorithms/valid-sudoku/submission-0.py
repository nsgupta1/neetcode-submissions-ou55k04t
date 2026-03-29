class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                curr = board[i][j]
                if curr == ".":
                    continue
                if(curr in row[i] or curr in col[j] or curr in grid[(i//3)*3+j//3]):
                    return False
                row[i].add(curr)
                col[j].add(curr)
                grid[(i//3)*3+j//3].add(curr)
        
        return True