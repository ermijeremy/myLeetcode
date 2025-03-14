class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i!=']':
                stack.append(i)
            else:
                cur = ''
                while stack[-1]!='[':
                    cur = stack[-1]+cur
                    stack.pop()
                stack.pop()
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num)*cur)
        return ''.join(stack)