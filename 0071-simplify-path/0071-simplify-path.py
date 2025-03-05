class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for i in path:
            if i == '..' and stack:
                stack.pop()
            elif i!='.' and i!='' and i!='..':
                stack.append(i)
        stack = '/'.join(stack).rstrip('/')
        stack = '/'+stack
        return stack