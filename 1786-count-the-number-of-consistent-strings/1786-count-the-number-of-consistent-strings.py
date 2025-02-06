class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        diA = set(allowed)
        count = 0
        for i in words:
            diW = Counter(set(i))
            if len(set(i)-diA)==0:
                count+=1
        return count
