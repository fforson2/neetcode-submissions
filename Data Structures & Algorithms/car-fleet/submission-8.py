class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        fleets = 1

        prevTime = (target - pair[0][0])/pair[0][1]

        for i in range(len(pair)):
            currTime = (target - pair[i][0])/pair[i][1]

            #Cannot catch up hence forms a new fleet
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

            #No else because we merge them as a fleet and move on to the next iteration of the loop

        return fleets


