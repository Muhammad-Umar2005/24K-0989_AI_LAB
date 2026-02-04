class SecurityAgent:
    def __init__(self,agent_id,name,status):
        self.agent_id=agent_id
        self.name=name
        self.status=status

class FirewallAgent(SecurityAgent):
    def monitor_traffic(self):
        print(self.name,"is monitoring network traffic")

class MalwareDetectionAgent(SecurityAgent):
    def scan_files(self):
        print(self.name,"is scanning files for malware")

class AutomationAgent(SecurityAgent):
    def run_automation(self):
        print(self.name,"is running security automation")

fw=FirewallAgent(1,"FirewallAgent","Active")
md=MalwareDetectionAgent(2,"MalwareAgent","Active")
au=AutomationAgent(3,"AutomationAgent","Active")

fw.monitor_traffic()
md.scan_files()
au.run_automation()