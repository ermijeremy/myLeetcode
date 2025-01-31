class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for i in range(len(operations)):
            if "+" in operations[i]:
                result += 1
            else:
                result -= 1
        return result