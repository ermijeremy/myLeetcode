class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        j=1
        if not strs:
            return ""
        mini = min(strs,key=len)
        for i in range(len(strs[0])):
            temp = strs[0][0:j]
            for n in range(1,len(strs)):
                if temp != strs[n][0:j]:
                    print("hi")
                    return result
            result = temp
            j+=1
        return result