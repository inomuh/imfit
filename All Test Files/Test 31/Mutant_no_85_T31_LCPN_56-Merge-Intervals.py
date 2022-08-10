class Solution:
    def merge(intervals):
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append( )
        return output

print(Solution.merge(intervals = [[1,4],[4,5]]))