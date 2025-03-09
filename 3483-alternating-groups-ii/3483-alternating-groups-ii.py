class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        di = {}
        j = i = 0
        n = len(colors)
        while i in range(n):
            count = 1
            first = (colors[i],j)
            while i < n-1 and colors[i]!=colors[i+1]:
                count += 1
                i += 1
            else:
                i += 1
            j+=1
            if count >= k:
                di[first] = [count,1]
            else:
                di[first] = [count,-1]

        last = sum([i[0]-k+1 for i in di.values() if i[1]>0])
        di = list(map(list,di.items()))
        if n>=k:
            l = colors[n-k+1:]+colors[:k-1]
            di1 = {}
            j = i = 0
            m = len(l)
            while i in range(m):
                count = 1
                first = (l[i],j)
                while i < m-1 and l[i]!=l[i+1]:
                    count += 1
                    i += 1
                else:
                    i += 1
                j+=1
                if count >= k:
                    di1[first] = [count,1]
                else:
                    di1[first] = [count,-1]
            last1 = sum([i[0]-k+1 for i in di1.values() if i[1]>0])
            di1 = list(map(list,di1.items()))
        last += last1
            
            
        if len(di)==1 and n%2==0:
            return n
        
        if last<0:
            return 0
        return last

        