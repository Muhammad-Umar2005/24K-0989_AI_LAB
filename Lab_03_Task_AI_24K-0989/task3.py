import random
class Environment:
    def __init__(self):
        self.backuplist={}
        self.servers = ['Server-1', 'Server-2', 'Server-3', 'Server-4', 'Server-5']
        for server in self.servers: # fr 10 records
            self.backuplist[server] = random.choice(['Completed','Failed'])
    
    def get_percept(self,server):
        return self.backuplist[server]
    
    def update(self,newrecord,server):
        self.backuplist[server]=newrecord


    def Display(self,state):
        print(state)
        print()
        for server in self.servers:
            print(f"Record of {server} : {self.backuplist[server]}")
            print()

class BackUpManagementAgent:
   
   def act(self,percept):
            if percept=='Completed':
                print("Backup is Completed")
                return 'Completed'
            else:
                print("Backup is failed.")
                print("Retry backup...")
                return 'Completed'

def Agent(Environment,BackUpManagementAgent):
    Environment.Display("---Initial State---")
    for server in Environment.servers:
        percept=Environment.get_percept(server)
        update=BackUpManagementAgent.act(percept)
        Environment.update(update,server)

    print()
    Environment.Display("---Final State---")

env=Environment()
BMA=BackUpManagementAgent()
Agent(env,BMA)

