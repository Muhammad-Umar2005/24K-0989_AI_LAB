# TASK 2 - A* Search with Dynamic Edge Costs
import heapq
import random
import time

class AdaptiveAStar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.edge_costs = {}
        for u in graph:
            for v in graph[u]:
                self.edge_costs[(u,v)] = graph[u][v]
    
    def dynamic_cost_update(self):
        for u in self.graph:
            for v in self.graph[u]:
                if random.random() < 0.01:
                    change = random.uniform(0.5, 2.0)
                    self.edge_costs[(u,v)] = max(0.1, self.edge_costs[(u,v)] * change)
    
    def heuristic(self, node):
        return abs(node[0]-self.goal[0]) + abs(node[1]-self.goal[1])
    
    def get_neighbors(self, node):
        if node in self.graph:
            return [(nei, self.edge_costs[(node, nei)]) for nei in self.graph[node]]
        return []
    
    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]
    
    def search(self, max_iterations=1000):
        open_set = [(self.heuristic(self.start), 0, self.start)]
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}
        open_hash = {self.start}
        
        for _ in range(max_iterations):
            self.dynamic_cost_update()
            
            if not open_set:
                return None
            
            current_f, current_g, current = heapq.heappop(open_set)
            open_hash.discard(current)
            
            if current == self.goal:
                return self.reconstruct_path(came_from, current)
            
            for neighbor, cost in self.get_neighbors(current):
                tentative_g = g_score[current] + cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor)
                    if neighbor not in open_hash:
                        heapq.heappush(open_set, (f_score[neighbor], tentative_g, neighbor))
                        open_hash.add(neighbor)
            
            time.sleep(0.05)
        return None
    
    def continuous_search(self):
        path = None
        while path is None or path[-1] != self.goal:
            if path and len(path) > 1:
                self.start = path[1]
            path = self.search(max_iterations=50)
            if path:
                print(f"Path updated: {path[:3]}...{path[-3:]}")
        return path

graph = {
    (0,0): { (0,1): 1, (1,0): 1 },
    (0,1): { (0,0): 1, (0,2): 1, (1,1): 1.5 },
    (0,2): { (0,1): 1, (0,3): 1, (1,2): 1.2 },
    (0,3): { (0,2): 1, (1,3): 1 },
    (1,0): { (0,0): 1, (1,1): 1, (2,0): 1 },
    (1,1): { (1,0): 1, (0,1): 1.5, (1,2): 1, (2,1): 1 },
    (1,2): { (1,1): 1, (0,2): 1.2, (1,3): 1, (2,2): 1 },
    (1,3): { (1,2): 1, (0,3): 1, (2,3): 1 },
    (2,0): { (1,0): 1, (2,1): 1, (3,0): 1 },
    (2,1): { (2,0): 1, (1,1): 1, (2,2): 1, (3,1): 1 },
    (2,2): { (2,1): 1, (1,2): 1, (2,3): 1, (3,2): 1 },
    (2,3): { (2,2): 1, (1,3): 1, (3,3): 1 },
    (3,0): { (2,0): 1, (3,1): 1 },
    (3,1): { (3,0): 1, (2,1): 1, (3,2): 1 },
    (3,2): { (3,1): 1, (2,2): 1, (3,3): 1 },
    (3,3): { (3,2): 1, (2,3): 1 }
}
start = (0,0)
goal = (3,3)
solver = AdaptiveAStar(graph, start, goal)
final_path = solver.continuous_search()
print("Final path:", final_path)