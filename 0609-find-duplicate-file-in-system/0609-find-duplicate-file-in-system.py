class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        di = {}
        for i in paths:
            temp = i.split()
            for j in range(1,len(temp)):
                tempo = temp[j]
                index = tempo.index('(')+1
                key = tempo[index:-1]
                di[key] = di.get(key,[]) + [temp[0]+"/"+tempo[0:index-1]]
        for i in di.values():
            if len(i)>1:
                ans.append(i)
        return ans