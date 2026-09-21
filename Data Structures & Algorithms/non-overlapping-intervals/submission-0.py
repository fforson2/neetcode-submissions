class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort according to start times
        intervals = sorted(intervals, key = lambda x: x[0])
        prevEnd = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):

            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1

            else:
                prevEnd = intervals[i][1]

        return count
