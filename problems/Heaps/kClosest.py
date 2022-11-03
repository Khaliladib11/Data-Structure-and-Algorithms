# MinHeap applicartion
# K Closest Points to Origin
# Leetcode 973: https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculateDistance(point):
            return sqrt(point[0]**2 + point[1]**2)
        
        minHeap = []
        
        for point in points:
            dist = calculateDistance(point)
            minHeap.append([dist, point[0], point[1]])
            
        
        heapq.heapify(minHeap)
        output = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            output.append([x, y])
            k -= 1
            
        return output  
            
        
             