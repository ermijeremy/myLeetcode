class Solution:
    def minMoves(self, target: int, d: int) -> int:

        move = 0
        while d and target>2:
            if target%2:
                move += 2
            else:
                move += 1
            target = target//2
            d -= 1

        return move + target-1