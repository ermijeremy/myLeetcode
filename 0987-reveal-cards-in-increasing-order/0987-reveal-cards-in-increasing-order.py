class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque([i for i in range(len(deck))])
        ans1 = [0]*(len(deck)+1)

        for i in range(len(deck)):
            ans1[ans[0]] = deck[i]
            a = ans.popleft()
            if not ans:
                break
            b = ans.popleft()
            ans.append(b)

        ans1.pop()
        return(ans1)
                

            

