class Solution:
    def maskPII(self, s: str) -> str:
        def mail(s):
            a = []
            i = s.index('@')
            o = s.index('.')
            a.append(s[0].lower())
            a.append("*****")
            a.append(s[i-1].lower())
            a.append("@")
            for j in s[i+1:]:
                a.append(j.lower())
            return(str(''.join(a)))
        def number(s):
            a = []
            c = []
            count = 0
            count1 = 0
            for i in s:
                if i.isdigit():
                    count1+=1
            b = count1-10
            if b>0:
                a.append("+")
                for i in range((b)):
                    a.append("*")
                a.append("-***-***-")
            else:
                a.append("***-***-")
            for i in s[::-1]:
                if count == 4:
                    break
                if i.isdigit():
                    c.append(i)
                    count+=1
            c = str(''.join(c[::-1]))
            a = str(''.join(a))
            return(a+c)
        if s[0].isdigit() or s[0]=="+" or s[0]=="(" or s[0]==")" or s[0]=="-" or s[0]==" ":
            return number(s)
        else:
            return mail(s)
