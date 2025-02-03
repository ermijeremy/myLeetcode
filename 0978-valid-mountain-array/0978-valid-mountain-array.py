class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        flag = True
        for i in range(len(arr)-1):
            if arr[0]>arr[1]:
                return False
            if arr[i]==arr[i+1]:
                return False
            if not flag:
                if arr[i]<arr[i+1]:
                    return False
            if flag:
                if arr[i]>arr[i+1]:
                    flag = False
        if flag:
            return False
        return True
