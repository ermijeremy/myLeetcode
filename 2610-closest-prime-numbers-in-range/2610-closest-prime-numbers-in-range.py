class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(max_num):
            is_prime = [True] * (max_num + 1)
            p = 2
            while (p * p <= max_num):
                if is_prime[p]:
                    for i in range(p * p, max_num + 1, p):
                        is_prime[i] = False
                p += 1
            prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
            return prime_numbers

        def primes_between(start, end):
            if start > end:
                return []
            primes = sieve_of_eratosthenes(end)
            return [p for p in primes if p >= start]

        res = primes_between(left,right)

        l,r = 0,len(res)-1
        ans = []

        while l<r:
            if not ans:
                ans.append([res[l],res[r]])
            else:
                a,b = ans[-1]
                ans.append([res[l],res[r]])
                ans.append([a,res[r]])
                ans.append([res[l],a])
                ans.append([res[r],b])
                ans.append([res[l],b])
            l += 1
            r -= 1
        if not ans:
            return [-1,-1]
        ans.sort(key = lambda x:abs(x[0]-x[1]))
        minn = abs(ans[0][1]-ans[0][0])
        ans1 = []
        for i,j in ans:
            if abs(j-i)==minn:
                ans1.append([i,j])
            else:
                break
        ans1.sort()
        return [min(ans1[0]),max(ans1[0])]