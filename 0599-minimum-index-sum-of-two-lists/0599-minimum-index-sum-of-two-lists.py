class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        di = {}
        ans = []
        for i in range(len(list1)):
            if list1[i] in list2:
                temp = list2.index(list1[i])
                di[i] = i+temp
        
        minn = min(di.values())
        for i,j in di.items():
                if j==minn:
                    ans.append(list1[i])
        return ans