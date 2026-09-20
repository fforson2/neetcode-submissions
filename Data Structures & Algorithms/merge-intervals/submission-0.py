class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #start according to start times
        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]]

        for start, end in intervals:
            if output[-1][1] >= start:
                endOfTime = max(end, output[-1][-1])
                output[-1] = [output[-1][0], endOfTime]
            else:
                output.append([start, end])

        return output