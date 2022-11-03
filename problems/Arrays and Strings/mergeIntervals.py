# Merge Intervals
# Leetcode 56: https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_output = output[-1]
            if intervals[i][0] <= last_output[1]:
                output[-1][1] = max(intervals[i][1], last_output[1])
            else:
                output.append(intervals[i])
                
        
        return output