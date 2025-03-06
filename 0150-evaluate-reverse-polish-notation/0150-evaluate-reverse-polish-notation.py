class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
            elif i == '-':
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
            elif i == '*':
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
            elif i == '/':
                if stack:
                    print(stack,'/')
                    a = stack.pop()
                    b = stack.pop()
                    if b<0 and abs(b)>a and a>=0:
                        stack.append(-(abs(b)//a))
                    elif (b < 0 and a > 0) or (a==0):
                        stack.append(0)
                    elif b < 0 and a<0:
                        stack.append(abs(b)//abs(a))
                    else:
                        if b/a < 0:
                            stack.append(math.ceil(b/a))
                        else:
                            stack.append(b//a)
                    print(stack,'//')
            else:
                stack.append(int(i))

        return stack[0]