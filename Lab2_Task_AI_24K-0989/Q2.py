class Threat:
    def __init__(self,threat_id,name,severity):
        self.threat_id=threat_id
        self.name=name
        self.severity=severity

class PhishingThreat(Threat):
    def analyze_email(self):
        print(self.name,"is analyzing emails")

    def result(self):
        print(f"Severity is {self.severity}")

class RansomwareThreat(Threat):
    def scan_files(self):
        print(self.name,"is scanning file system")

    def result(self):
        print(f"Severity is {self.severity}")

class BotnetThreat(Threat):
    def detect_traffic(self):
        print(self.name,"is detecting network traffic")

    def result(self):
        print(f"Severity is {self.severity}")


p=PhishingThreat(101,"Phishing","High")
r=RansomwareThreat(102,"Ransomware","Critical")
b=BotnetThreat(103,"Botnet","Medium")

p.analyze_email()
p.result()
print()
r.scan_files()
r.result()
print()
b.detect_traffic()
b.result()
