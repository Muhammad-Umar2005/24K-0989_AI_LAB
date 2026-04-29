
# TASK 3 - Delivery Route Optimization with Time Windows
from datetime import datetime, timedelta

class DeliveryOptimizer:
    def __init__(self, locations, start_point, time_windows, travel_times):
        self.locations = locations
        self.start = start_point
        self.time_windows = time_windows
        self.travel_times = travel_times
    
    def calculate_deadline_priority(self, location, current_time):
        window_open, window_close = self.time_windows[location]
        if current_time > window_close:
            return -float('inf')
        urgency = (window_close - current_time).total_seconds()
        return -urgency
    
    def greedy_best_first_search(self):
        unvisited = set(self.locations)
        current_pos = self.start
        current_time = datetime(2024,1,1,8,0,0)
        route = [self.start]
        total_distance = 0
        
        while unvisited:
            best_candidate = None
            best_score = -float('inf')
            best_path = None
            best_new_time = None
            
            for loc in unvisited:
                travel = self.travel_times.get((current_pos, loc), self.travel_times.get((loc, current_pos), float('inf')))
                arrival_time = current_time + timedelta(minutes=travel)
                window_open, window_close = self.time_windows[loc]
                
                if arrival_time > window_close:
                    continue
                
                wait_time = max(0, (window_open - arrival_time).total_seconds()/60.0)
                actual_arrival = arrival_time + timedelta(minutes=wait_time)
                
                priority = self.calculate_deadline_priority(loc, actual_arrival)
                
                if priority > best_score:
                    best_score = priority
                    best_candidate = loc
                    best_path = travel
                    best_new_time = actual_arrival
            
            if best_candidate is None:
                return None, None
            
            route.append(best_candidate)
            total_distance += best_path
            current_time = best_new_time
            unvisited.remove(best_candidate)
            current_pos = best_candidate
        
        return route, total_distance
    
    def optimize_with_distance_awareness(self):
        unvisited = set(self.locations)
        current_pos = self.start
        current_time = datetime(2024,1,1,8,0,0)
        route = [self.start]
        total_distance = 0
        
        while unvisited:
            candidates = []
            for loc in unvisited:
                travel = self.travel_times.get((current_pos, loc), self.travel_times.get((loc, current_pos), float('inf')))
                arrival_time = current_time + timedelta(minutes=travel)
                window_open, window_close = self.time_windows[loc]
                
                if arrival_time > window_close:
                    continue
                
                wait_time = max(0, (window_open - arrival_time).total_seconds()/60.0)
                schedule_penalty = wait_time * 2
                deadline_urgency = (window_close - arrival_time).total_seconds() / 60.0
                distance_factor = travel
                
                score = - (deadline_urgency * 0.7 + distance_factor * 0.3 - schedule_penalty)
                candidates.append((score, loc, travel, arrival_time + timedelta(minutes=wait_time)))
            
            if not candidates:
                return None, None
            
            candidates.sort()
            best_score, best_loc, best_travel, best_time = candidates[0]
            
            route.append(best_loc)
            total_distance += best_travel
            current_time = best_time
            unvisited.remove(best_loc)
            current_pos = best_loc
        
        return route, total_distance

if __name__ == "__main__":
    locations = ['A', 'B', 'C', 'D', 'E']
    start_point = 'Warehouse'
    time_windows = {
        'Warehouse': (datetime(2024,1,1,8,0,0), datetime(2024,1,1,20,0,0)),
        'A': (datetime(2024,1,1,9,0,0), datetime(2024,1,1,10,0,0)),
        'B': (datetime(2024,1,1,10,30,0), datetime(2024,1,1,12,0,0)),
        'C': (datetime(2024,1,1,13,0,0), datetime(2024,1,1,14,30,0)),
        'D': (datetime(2024,1,1,11,0,0), datetime(2024,1,1,13,0,0)),
        'E': (datetime(2024,1,1,15,0,0), datetime(2024,1,1,16,30,0))
    }
    travel_times = {
        ('Warehouse', 'A'): 25, ('Warehouse', 'B'): 40, ('Warehouse', 'C'): 60,
        ('Warehouse', 'D'): 35, ('Warehouse', 'E'): 50,
        ('A', 'B'): 20, ('A', 'C'): 45, ('A', 'D'): 30, ('A', 'E'): 55,
        ('B', 'C'): 30, ('B', 'D'): 25, ('B', 'E'): 40,
        ('C', 'D'): 35, ('C', 'E'): 25, ('D', 'E'): 30
    }
    
    optimizer = DeliveryOptimizer(locations, start_point, time_windows, travel_times)
    route1, dist1 = optimizer.greedy_best_first_search()
    route2, dist2 = optimizer.optimize_with_distance_awareness()
    
    print("Greedy deadline-first route:", route1, "Distance:", dist1)
    print("Optimized route:", route2, "Distance:", dist2)