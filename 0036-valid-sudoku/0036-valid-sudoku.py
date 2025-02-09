class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = set()
        di = defaultdict(tuple)
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        t = board[i][j]
                        if t.isdigit():
                            if t in temp:
                                return False
                            if t in di:
                                if i in di[t][0] or j in di[t][1]:
                                    return False
                                else:
                                    di[t][0] += [i]
                                    di[t][1] += [j]
                            else:
                                di[t] = [[i]]
                                di[t] += [[j]]
                            temp.add(t)
                temp = set()

        return True