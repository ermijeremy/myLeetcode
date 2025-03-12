class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):
            if n==0:
                return 1
            elif n%2:
                return x*recur(x**2,(n-1)//2)
            if n%2==0:
                return recur(x**2,n//2)
        def recur1(x,n):
            if n==0:
                return 1
            elif n%2:
                return 1/x*(1/recur(x**2,(n-1)//2))
            if n%2==0:
                return recur(1/(x**2),n//2)
        return recur(x,n) if n>=0 else recur1(x,abs(n))
