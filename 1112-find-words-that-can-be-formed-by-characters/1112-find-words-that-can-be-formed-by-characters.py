class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        diC = Counter(chars)
        count = 0
        for i in words:
            diW = Counter(i)
            if not diW - diC:
                count += len(i)
        return count