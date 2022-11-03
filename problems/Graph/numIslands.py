# BFS applicartion
# Number of Islands
# Leetcode 200: https://leetcode.com/problems/number-of-islands/


from collections import deque


class Solution:
    def numIslands(self, grid: list) -> int:

        visited = set()  # to keep track of visited cells
        island = 0  # to keep track of the number of island
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            directions = [[-1, 0], [+1, 0], [0, -1], [0, +1]]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r_ , c_ = dr + row, dc + col

                    if (r_ in range(rows) and 
                        c_ in range(cols) and
                        grid[r_][c_] == '1' and
                        (r_, c_) not in visited
                    ):
                        queue.append((r_, c_))
                        visited.add((r_, c_))

                         

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    island += 1
                    island

        return island