class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a = list(zip(*trips))
        temp = [0]*(max(a[2])+1)
        for i,j,k in trips:
            temp[j] += i
            temp[k] += -i
        temp = list(itertools.accumulate(temp))
        
        return max(temp) <= capacity