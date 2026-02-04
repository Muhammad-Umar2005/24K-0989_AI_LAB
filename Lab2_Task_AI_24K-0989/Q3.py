class ResponseAgent:
    def execute_response(self):
        print("Executing a general response...")


class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("AlertAgent: Sending security alert notifications.")


class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("BlockAgent: Blocking malicious activity.")


class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("RecoverAgent: Restoring affected systems.")



agents = [
    AlertAgent(),
    BlockAgent(),
    RecoverAgent()
]


for agent in agents:
    agent.execute_response()
