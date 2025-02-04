class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        di = defaultdict(int)
        ans = []
        for i in cpdomains:
            count,eachS = i.split()
            eachD = eachS.split(".")
            for j in range(len(eachD)):
                di[".".join(eachD[j:])] += int(count)
        for i in di.items():
            ans.append(f"{i[1]} {i[0]}")
        return ans