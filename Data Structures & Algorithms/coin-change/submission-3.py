class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([0])
        seen = [False] * (amount + 1)
        res = 0
        seen[0] = True

        while q:
            res += 1
            for i in range(len(q)):
                curr = q.popleft()
                for coin in coins:
                    nxt = coin + curr
                    if nxt == amount:
                        return res

                    if nxt > amount or seen[nxt] :
                        continue
                    
                    q.append(nxt)
                    seen[nxt] = True

        return -1
                
