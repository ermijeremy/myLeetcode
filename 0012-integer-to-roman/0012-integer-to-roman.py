class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        ex = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I",900:"CM",400:"CD",90:"XC",40:"XL",9:"IX",4:"IV"}
        num = str(num)
        print(num[0])
        for i in range(len(num)):
            val = 10**(len(num)-i-1)
            if int(num[i])*val in ex:
                ans.append(ex[int(num[i])*val])
            else:
                if int(num[i])<5:
                    for j in range(int(num[i])):
                        ans.append(ex[val])
                else:
                    ans.append(ex[val*5])
                    for j in range(int(num[i])-5):
                        ans.append(ex[val])
        return ''.join(ans)