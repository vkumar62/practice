from collections import deque
import pdb
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        if not image or image[sr][sc] == newColor:
            return image
        
        pdb.set_trace()
        # Original color itself can be used for visited check
        # Perform a BFS
        q = deque()
        orig_color = image[sr][sc]
        q.append((sr, sc))
        
        while q:
            r, c = q.popleft()
            if image[r][c] != orig_color:
                continue
            image[r][c] = newColor
            # Add all neighbors to the queue
            neighbors = [(x,y) for x, y in ((r-1, c), (r, c-1), (r, c+1), (r+1, c)) if 0 <= x < len(image) and 0 <= y < len(image[0])]
            for neighbor in neighbors:
                q.append(neighbor)
                
        return image

print(Solution().floodFill([[0,0,0],[0,1,1]],
1,
1,
1))
