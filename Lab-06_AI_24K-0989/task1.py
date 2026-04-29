# TASK 1 - Enhanced Maze Navigation with Multiple Goals
import heapq

class EnhancedMazeNav:
    def __init__(self, maze, start, goals):
        self.maze = maze
        self.start = start
        self.goals = set(goals)
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def manhattan(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    def shortest_path(self, start, end):
        heap = [(self.manhattan(start, end), 0, start, [start])]
        visited = set()
        while heap:
            _, cost, pos, path = heapq.heappop(heap)
            if pos == end:
                return path
            if pos in visited:
                continue
            visited.add(pos)
            for dr, dc in self.directions:
                nr, nc = pos[0]+dr, pos[1]+dc
                if 0<=nr<self.rows and 0<=nc<self.cols and self.maze[nr][nc]!=1:
                    new_pos = (nr, nc)
                    if new_pos not in visited:
                        heapq.heappush(heap, (self.manhattan(new_pos, end)+cost+1, cost+1, new_pos, path+[new_pos]))
        return None
    
    def tsp_shortest_covering(self):
        all_points = [self.start] + sorted(list(self.goals))
        n = len(all_points)
        dist_matrix = [[0]*n for _ in range(n)]
        path_cache = {}
        for i in range(n):
            for j in range(i+1, n):
                p = self.shortest_path(all_points[i], all_points[j])
                if p:
                    dist_matrix[i][j] = len(p)-1
                    dist_matrix[j][i] = len(p)-1
                    path_cache[(i,j)] = p
                    path_cache[(j,i)] = p[::-1]
                else:
                    return None
        
        dp = [[float('inf')]*n for _ in range(1<<n)]
        parent = [[-1]*n for _ in range(1<<n)]
        dp[1][0] = 0
        for mask in range(1<<n):
            for u in range(n):
                if dp[mask][u] == float('inf'):
                    continue
                for v in range(n):
                    if not (mask>>v & 1) and dist_matrix[u][v] < float('inf'):
                        new_mask = mask | (1<<v)
                        new_cost = dp[mask][u] + dist_matrix[u][v]
                        if new_cost < dp[new_mask][v]:
                            dp[new_mask][v] = new_cost
                            parent[new_mask][v] = u
        
        final_mask = (1<<n)-1
        best_end = 0
        best_cost = float('inf')
        for i in range(1,n):
            if dp[final_mask][i] < best_cost:
                best_cost = dp[final_mask][i]
                best_end = i
        
        if best_cost == float('inf'):
            return None
        
        path = []
        mask = final_mask
        curr = best_end
        while curr != -1:
            path.append(curr)
            prev = parent[mask][curr]
            mask = mask & ~(1<<curr)
            curr = prev
        path.reverse()
        
        full_path = []
        for i in range(len(path)-1):
            seg = path_cache[(path[i], path[i+1])]
            if full_path and seg[0] == full_path[-1]:
                full_path.extend(seg[1:])
            else:
                full_path.extend(seg)
        return full_path

maze = [
    [0,0,0,1,0],
    [0,1,0,1,0],
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,0,0,0,0]
]
start = (0,0)
goals = [(4,4), (0,2), (2,4)]
solver = EnhancedMazeNav(maze, start, goals)
result = solver.tsp_shortest_covering()
print("Path covering all goals:", result)