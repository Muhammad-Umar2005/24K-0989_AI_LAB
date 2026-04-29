# TASK #1 - Depth-Limited Search as Goal-Based Agent
class DLSAgent:
    def __init__(self, graph, limit):
        self.graph = graph
        self.limit = limit
    
    def search(self, start, goal):
        return self.dls(start, goal, 0)
    
    def dls(self, node, goal, depth):
        if node == goal:
            return [node]
        if depth == self.limit:
            return None
        for neighbor in self.graph.get(node, []):
            result = self.dls(neighbor, goal, depth + 1)
            if result is not None:
                return [node] + result
        return None

# TASK #1 - Uniform Cost Search as Utility-Based Agent
class UCSAgent:
    def __init__(self, graph):
        self.graph = graph
    
    def search(self, start, goal):
        frontier = [(0, start, [start])]
        explored = set()
        while frontier:
            frontier.sort()
            cost, node, path = frontier.pop(0)
            if node in explored:
                continue
            explored.add(node)
            if node == goal:
                return path, cost
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in explored:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    frontier.append((new_cost, neighbor, new_path))
        return None, None

# TASK #3 - Iterative Deepening DFS on Graph and Tree
class IDDFSAgent:
    def __init__(self, graph):
        self.graph = graph
    
    def dls(self, node, goal, depth):
        if node == goal:
            return [node]
        if depth <= 0:
            return None
        for neighbor in self.graph.get(node, []):
            result = self.dls(neighbor, goal, depth - 1)
            if result is not None:
                return [node] + result
        return None
    
    def iddfs_graph(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            result = self.dls(start, goal, depth)
            if result is not None:
                return result
        return None
    
    def iddfs_tree(self, tree_root, goal, max_depth):
        def dls_tree(node, goal, depth):
            if node == goal:
                return [node]
            if depth <= 0:
                return None
            for child in tree_root.get(node, []):
                result = dls_tree(child, goal, depth - 1)
                if result is not None:
                    return [node] + result
            return None
        
        for depth in range(max_depth + 1):
            result = dls_tree(list(tree_root.keys())[0], goal, depth)
            if result is not None:
                return result
        return None

graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [7], 6: [], 7: []}
weighted_graph = {1: [(2, 2), (3, 5)], 2: [(4, 3), (5, 4)], 3: [(6, 6)], 4: [], 5: [(7, 1)], 6: [], 7: []}
tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7: []}

print("=== Depth Limited Search ===")
agent1 = DLSAgent(graph, 3)
result1 = agent1.search(1, 7)
print("Path found:", result1)

print("\n=== Uniform Cost Search ===")
agent2 = UCSAgent(weighted_graph)
path2, cost2 = agent2.search(1, 7)
print("Path found:", path2)
print("Total cost:", cost2)

print("\n=== Iterative Deepening DFS on Graph ===")
agent3 = IDDFSAgent(graph)
result3 = agent3.iddfs_graph(1, 7, 5)
print("Path found:", result3)

print("\n=== Iterative Deepening DFS on Tree ===")
result4 = agent3.iddfs_tree(tree, 7, 5)
print("Path found:", result4)