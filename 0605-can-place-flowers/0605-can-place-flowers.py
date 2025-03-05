class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        flow = list(map(str,flowerbed))
        flow = ''.join(flow).split('1')
        ans = 0
        for i in flow:
            a = i.count('0')
            if a==3:
                ans += 1
            elif a > 3:
                ans += ((a-3)//2)+1
        
        return n<=ans