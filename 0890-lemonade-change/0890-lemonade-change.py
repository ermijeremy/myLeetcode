class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        di = defaultdict(int)

        for i in range(len(bills)):
            
            if bills[i] == 20:
                if ((di[10]>=1) and (di[5]>=1)):
                    di[10] -= 1
                    di[5] -= 1
                elif di[5] >= 3:
                    di[5] -= 3
                else:
                    return False

            elif bills[i]==10:
                if di[5] >= 1:
                    di[5] -= 1
                    di[10] += 1
                else:
                    return False
            else:
                di[5] += 1

        return True