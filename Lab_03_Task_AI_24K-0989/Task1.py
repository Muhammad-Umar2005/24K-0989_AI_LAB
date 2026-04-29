import random

class Environment:
    def __init__(self):
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.state = {}
        for comp in self.components:
            self.state[comp] = random.choice(['Safe', 'Vulnerable'])
    
    def get_percept(self, component):
        return self.state[component]
    
    def patch_component(self, component):
        self.state[component] = 'Safe'
    
    def display_state(self, title):
        print("\n" + "="*50)
        print(title)
        print("="*50)
        for comp in self.components:
            status = self.state[comp]
            if status == 'Safe':
                icon = "\/"
            else:
                icon = "✗"
            print(f"  Component {comp}: {icon} {status}")

class SecurityAgent:
    def __init__(self):
        self.vulnerable_list = []
    
    def act(self, percept, component):
        if percept == 'Vulnerable':
            self.vulnerable_list.append(component)
            return f"Component {component} is VULNERABLE - Will patch"
        else:
            return f"Component {component} is SAFE - No action"
    
    def patch_all(self, environment):
        if len(self.vulnerable_list) == 0:
            return "Nothing to patch"
        
        for comp in self.vulnerable_list:
            environment.patch_component(comp)
        
        return f"Patched: {', '.join(self.vulnerable_list)}"

def run_agent(agent, environment, steps):
    print("CYBERSECURITY SIMULATION")
    
    environment.display_state("INITIAL SYSTEM CHECK")
    
    print("\n" + "="*50)
    print("SCANNING SYSTEM")
    print("="*50)
    
    for step in range(steps):
        component = environment.components[step]
        percept = environment.get_percept(component)
        action = agent.act(percept, component)
        print(f"Step {step + 1}: {percept} -> {action}")
    
    print("\n" + "="*50)
    print("PATCHING")
    print("="*50)
    result = agent.patch_all(environment)
    print(result)
    
    environment.display_state("FINAL SYSTEM CHECK")
    
    print("\n" + "="*50)
    all_safe = True
    for comp in environment.components:
        if environment.state[comp] == 'Vulnerable':
            all_safe = False
    
    if all_safe:
        print("SYSTEM SECURE - All patched!")
    else:
        print("WARNING - Still vulnerable!")
    print("="*50)

agent = SecurityAgent()
environment = Environment()
run_agent(agent, environment, 9)