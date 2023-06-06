import subprocess
import socket

class NetworkScanner:
    def __init__(self):
        self.results = []

    
    def main(self):
        for adapter in self.get_adapters():
            self.results.append(adapter['ip'])
        return self.results
    

    def get_adapters(self):
        adapters = []
        result = subprocess.check_output(['ipconfig', '/all'])
        result = result.decode('utf-8').split('\n')
        for line in result:
            if 'IPv4' in line:
                adapter = {}
                adapter['name'] = line.split(':')[0] 
                adapter['ip'] = line.split(':')[1].strip()
                adapters.append(adapter)
        return adapters
    









