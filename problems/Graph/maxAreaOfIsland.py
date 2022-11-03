# BFS applicartion
# Max Area of Island
# Leetcode 695: https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        if not grid:
            return 0
        
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            a = 1
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r_ = dr+row
                    c_ = dc+col
                    if ((r_ in range(rows)) and 
                    (c_ in range(cols)) and 
                    ((r_, c_) not in visited) and
                    (grid[r_][c_] == 1)):
                        a += 1
                        visited.add((r_, c_))
                        q.append((r_, c_))
                        
            return a
        

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1 and (r, c) not in visited:
                    
                    area = bfs(r, c)
                    if area > max_area:
                        max_area = area
                        
        return max_area
                    