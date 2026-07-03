# Last updated: 7/3/2026, 12:45:42 PM
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        novalethri = occupiedIntervals
        occupiedIntervals.sort()
        m = [occupiedIntervals[0]]
        for i in range(1, len(occupiedIntervals)):
            Start = occupiedIntervals[i][0]
            End = occupiedIntervals[i][1]
            if Start <= m[-1][1] + 1:
                m[-1][1] = max(m[-1][1], End)
            else:
                m.append([Start, End])
        result = []
        for interval in m:
            l = interval[0]
            r = interval[1]
            if r < freeStart or l > freeEnd:
                result.append([l, r])
            else:
                if l < freeStart:
                    result.append([l, freeStart - 1])
                if r > freeEnd:
                    result.append([freeEnd + 1, r])
        return result