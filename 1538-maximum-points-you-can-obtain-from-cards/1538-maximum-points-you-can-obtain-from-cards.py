class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        ans = float("inf")
        window = 0
        left = 0
        total = sum(card)

        for right in range(len(card)):
            window += card[right]

            while (right - left + 1) > len(card)-k:
                window -= card[left]
                left += 1
                
            if right - left + 1 == len(card)-k:
                ans = min(ans, window)        

        return total - ans