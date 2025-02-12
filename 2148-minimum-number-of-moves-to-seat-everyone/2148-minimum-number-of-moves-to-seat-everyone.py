class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        a = [abs(seats[j]-students[j]) for j in range(len(seats))]
        return sum(a)