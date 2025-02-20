class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        count = 0
        
        left, right = 0, len(p)-1
        flag = True

        while left < right:
            temp = p[left]+p[right]

            if temp > limit:
                count += 1
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

            if left == right and p[left] <= limit:
                count += 1

        return count