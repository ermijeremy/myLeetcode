class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        one_cycle = n-1
        last_cycle = time//one_cycle
        remaining_move = time % one_cycle
        if last_cycle % 2 != 0:
            return n-remaining_move
        return remaining_move + 1