class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list(range(1,n+1))    
        return list(itertools.combinations(ans,k))