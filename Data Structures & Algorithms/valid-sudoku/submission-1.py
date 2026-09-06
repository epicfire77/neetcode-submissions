class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s == '.':
                    continue
                if s in row[r]:
                    return False
                if s in col[c]:
                    return False
                b = self.box(r, c)
                if s in box[b]:
                    return False
                row[r].add(s)
                col[c].add(s)
                box[b].add(s)
        return True
    def box(self, r, c):
        x = c // 3
        y = r // 3
        return x + y * 3