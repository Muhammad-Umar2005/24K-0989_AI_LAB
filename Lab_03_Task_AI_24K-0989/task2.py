import random

class Environment:
    def __init__(self):
        self.servers = ['Server-1', 'Server-2', 'Server-3', 'Server-4', 'Server-5']
        self.load = {}
        for server in self.servers:
            self.load[server] = random.choice(['Underloaded', 'Balanced', 'Overloaded'])
    
    def get_percept(self, server):
        return self.load[server]
    
    def set_load(self, server, new_load):
        self.load[server] = new_load
    
    def display_load(self, title):
        print("\n" + "="*50)
        print(title)
        print("="*50)
        for server in self.servers:
            status = self.load[server]
            print(f"  {server}: {status}")

class LoadBalancerAgent:
    def __init__(self):
        self.underloaded = []
        self.overloaded = []
    
    def act(self, percept, server):
        if percept == 'Underloaded':
            self.underloaded.append(server)
            return f"{server} is UNDERLOADED - Can receive tasks"
        elif percept == 'Overloaded':
            self.overloaded.append(server)
            return f"{server} is OVERLOADED - Must send tasks"
        else:
            return f"{server} is BALANCED - No action needed"
    
    def balance_load(self, environment):
        print("\n" + "="*50)
        print("BALANCING LOAD")
        print("="*50)
        
        moves = 0
        
        while len(self.overloaded) > 0 and len(self.underloaded) > 0:
            from_server = self.overloaded.pop(0)
            to_server = self.underloaded.pop(0)
            
            environment.set_load(from_server, 'Balanced')
            environment.set_load(to_server, 'Balanced')
            
            print(f"  Moved tasks from {from_server} to {to_server}")
            moves = moves + 1
        
        if moves == 0:
            print("  No balancing needed")
        else:
            print(f"  Total moves: {moves}")
        
        if len(self.overloaded) > 0:
            print(f"  Warning: {len(self.overloaded)} server(s) still overloaded")
        
        if len(self.underloaded) > 0:
            print(f"  Note: {len(self.underloaded)} server(s) still underloaded")

def run_agent(agent, environment, steps):
    print("LOAD BALANCER SIMULATION")
    
    environment.display_load("INITIAL LOAD STATUS")
    
    print("\n" + "="*50)
    print("SCANNING SERVERS")
    print("="*50)
    
    for step in range(steps):
        server = environment.servers[step]
        percept = environment.get_percept(server)
        action = agent.act(percept, server)
        print(f"Step {step + 1}: {action}")
    
    agent.balance_load(environment)
    
    environment.display_load("FINAL LOAD STATUS")
    
    print("\n" + "="*50)
    all_balanced = True
    for server in environment.servers:
        if environment.load[server] != 'Balanced':
            all_balanced = False
    
    if all_balanced:
        print("ALL SERVERS BALANCED!")
    else:
        print("SOME SERVERS NOT BALANCED")
    print("="*50)

agent = LoadBalancerAgent()
environment = Environment()
run_agent(agent, environment, 5)