# DFS applicartion
# Leetcode 733: https://leetcode.com/problems/flood-fill


class Solution:
    
    def dfs(self, image, sr, sc, first_color, new_color):
        
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) -1 or image[sr][sc] == new_color or image[sr][sc] != first_color:
            return
            
        
        image[sr][sc] = new_color
        self.dfs(image, sr-1, sc, first_color, new_color)
        self.dfs(image, sr+1, sc, first_color, new_color)
        self.dfs(image, sr, sc-1, first_color, new_color)
        self.dfs(image, sr, sc+1, first_color, new_color)
                
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color, new_color = image[sr][sc], color
        self.dfs(image, sr, sc, old_color, new_color)
        return image