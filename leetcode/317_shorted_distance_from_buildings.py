
from collections import deque
class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def empty_neighbors(x, y, grid):
            n = [(i, j) for i, j in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)) if 0 <= i < N and 0 <= j < M and grid[i][j] == 0]
            return n
        
        def calc_distances(building_idx, start, distances, grid):
            cur_q = deque()
            cur_q.append(start)
            visited = set(start)
            distance = 0
            
            while cur_q:
                next_q = deque()
                distance += 1
                while cur_q:
                    x,y = cur_q.popleft()
                    
                    for ex, ey in empty_neighbors(x,y, grid):
                        if (ex, ey) not in visited:
                            distances[ex][ey][building_idx] = distance
                            next_q.append((ex, ey))
                            visited.add((ex, ey))
                cur_q = next_q
            
        if not grid:
            return -1
        
        N = len(grid)
        M = len(grid[0])
        
        buildings = []
        
        # Scan and note down all the building locations
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    buildings.append((i,j))
        
        distances = [[[float('inf')] * len(buildings) for _ in range(M)]  for _ in range(N)]
        
        for i, building in enumerate(buildings):
            calc_distances(i, building, distances, grid)
            
        mindist = float('inf')
        for i in range(N):
            for j in range(M):
                mindist = min(mindist, sum(distances[i][j]))
        if mindist == float('inf'):
            return -1
        else:
            return mindist


grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(Solution().shortestDistance(grid))
grid = [[0,2,1],[1,0,2],[0,1,0]]
print(Solution().shortestDistance(grid))
